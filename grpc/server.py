import os
import sys

# Ensure project root is on PYTHONPATH so we can import shared utilities
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import grpc
from concurrent import futures
import subprocess
import service_pb2
import service_pb2_grpc
import time
from time_logger import setup as setup_logger

logger = setup_logger(__name__)

class PythonRunnerServicer(service_pb2_grpc.PythonRunnerServicer): 
    def __init__(self): 

        self.allowed_scripts = {
                # Map a script alias to the actual Python script we want to execute.
                # Adjust the relative path if your directory layout changes.
                'deepcrawl': 'deepcrawl.py' , 
                'main': 'main.py'
        }

    def ExecuteScript(self , request , context): 
        try : 
            start_time = time.time()
            logger.info(f"ExecuteScript called with script_name={request.script_name}, args={list(request.args)}")
            script_path = self.allowed_scripts.get(request.script_name)
            if not script_path : 
                duration = time.time() - start_time
                logger.warning(f"Unknown script '{request.script_name}' requested. Duration {duration:.2f}s")
                return service_pb2.ScriptResponse(
                        exit_code = 1 , 
                        stderr=f"Script did not ran" , 
                        success = False
                )

            # Build the command to run the requested Python script with arguments.
            # Use the "-u" flag to force the Python interpreter into *unbuffered* mode so 
            # that stdout/stderr are flushed immediately. This ensures the gRPC client
            # receives incremental output (otherwise you may only see the first line and
            # nothing afterwards until the process completes).
            cmd = [sys.executable, "-u", script_path] + list(request.args)

            result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd=PROJECT_ROOT,
            )

            # Log a preview of stdout/stderr for debugging
            stdout_preview = (result.stdout[:300] + '...') if len(result.stdout) > 300 else result.stdout
            stderr_preview = (result.stderr[:300] + '...') if len(result.stderr) > 300 else result.stderr
            logger.info(f"Stdout preview ({len(result.stdout)} chars): {stdout_preview}")
            if result.stderr:
                logger.warning(f"Stderr preview ({len(result.stderr)} chars): {stderr_preview}")

            duration = time.time() - start_time
            logger.info(
                f"Script {script_path} executed. Exit={result.returncode} Duration={duration:.2f}s"
            )

            return service_pb2.ScriptResponse(
                exit_code = result.returncode , 
                stdout = result.stdout , 
                stderr = result.stderr , 
                success= result.returncode == 0
            )

        except Exception as e:
            # Capture any unexpected server-side errors.
            return service_pb2.ScriptResponse(
                    exit_code=1 , 
                    stderr= str(e),
                    success= False
            )

    def ExecuteScriptStream(self, request, context):
        """Server-side streaming version of ExecuteScript.

        Streams stdout / stderr lines from the underlying script execution
        back to the client as they become available, followed by a final
        message that contains the exit code once the process terminates.
        """
        import select

        start_time = time.time()
        logger.info(
            "ExecuteScriptStream called with script_name=%s, args=%s",
            request.script_name,
            list(request.args),
        )

        script_path = self.allowed_scripts.get(request.script_name)
        if not script_path:
            yield service_pb2.ScriptResponse(
                exit_code=1,
                stderr=f"Unknown script '{request.script_name}' requested.",
                success=False,
            )
            return

        # Same unbuffered invocation for streaming execution
        cmd = [sys.executable, "-u", script_path] + list(request.args)

        try:
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=PROJECT_ROOT,
            )

            stdout_fd = proc.stdout.fileno() if proc.stdout else None
            stderr_fd = proc.stderr.fileno() if proc.stderr else None

            # Stream output until the process terminates and all output is consumed.
            while True:
                fds_to_read = []
                if stdout_fd is not None:
                    fds_to_read.append(proc.stdout)
                if stderr_fd is not None:
                    fds_to_read.append(proc.stderr)

                if not fds_to_read:
                    break

                readable, _, _ = select.select(fds_to_read, [], [], 0.1)

                for r in readable:
                    line = r.readline()
                    if line:
                        if r is proc.stdout:
                            logger.debug("stdout: %s", line.rstrip())
                            yield service_pb2.ScriptResponse(stdout=line, exit_code=-1)
                        else:
                            logger.debug("stderr: %s", line.rstrip())
                            yield service_pb2.ScriptResponse(stderr=line, exit_code=-1)

                if proc.poll() is not None and not readable:
                    # Process has finished and no more output to read.
                    break

            exit_code = proc.wait()
            duration = time.time() - start_time
            logger.info(
                "Script %s executed via stream. Exit=%s Duration=%.2fs",
                script_path,
                exit_code,
                duration,
            )

            yield service_pb2.ScriptResponse(
                exit_code=exit_code,
                success=exit_code == 0,
            )

        except Exception as e:
            logger.exception("Exception during ExecuteScriptStream: %s", e)
            yield service_pb2.ScriptResponse(
                exit_code=1,
                stderr=str(e),
                success=False,
            )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_PythonRunnerServicer_to_server(
            PythonRunnerServicer(), server
    )

    listen_addr = 'localhost:50051'
    server.add_insecure_port(listen_addr)


    logger.info(f"Starting gRPC server on {listen_addr}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__": 
    serve()
    



