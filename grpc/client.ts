import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import { performance } from 'perf_hooks';
import { log } from './logger';

const packageDefinition = protoLoader.loadSync('service.proto', {
	keepCase: true,
	longs: String,
	enums: String,
	defaults: true,
	oneofs: true,
});

const protoDescriptor = grpc.loadPackageDefinition(packageDefinition);
const pythonservice = protoDescriptor.pythonservice as any;

class PythonScriptRunner {
	private client: any;

	constructor(serverAddress: string = 'localhost:50051') {
		this.client = new pythonservice.PythonRunner(
			serverAddress,
			grpc.credentials.createInsecure()
		);
	}

	async executeScript(
		scriptName: string,
		args: string[] = [],
		envVars: Record<string, string> = {}
	): Promise<{
		exitCode: number;
		stdout: string;
		stderr: string;
		success: boolean;
	}> {
		return new Promise((resolve, reject) => {
			const startTime = performance.now();
			const request = {
				script_name: scriptName,
				args: args,
				env_vars: envVars,
			};

			this.client?.ExecuteScript(request, (error: any, response: any) => {
				if (error) {
					const duration = performance.now() - startTime;
					log(`gRPC error after ${duration.toFixed(0)} ms`, error);
					reject(error);
					return;
				}

				resolve({
					exitCode: response.exit_code,
					stdout: response.stdout,
					stderr: response.stderr,
					success: response.success,
				});

				const duration = performance.now() - startTime;
				log(`gRPC call completed in ${duration.toFixed(0)} ms (exitCode=${response.exit_code})`);
			});
		});
	}

	close() {
		this.client?.close();
	}
}

export default PythonScriptRunner;
