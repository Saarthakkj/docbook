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
                'deepcrawl': '../deepcrawl.py'
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
            cmd = [sys.executable, script_path] + list(request.args)


            # cmd = [sys.executable  , script_path] + list (request.args)



            result = subprocess.run(
                    cmd , 
                    capture_output = True , 
                    text = True , 
                    timeout = 300, 
                    cwd =  PROJECT_ROOT
            )

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


def serve():
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))
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
    



