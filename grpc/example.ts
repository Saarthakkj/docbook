import { performance } from 'perf_hooks';
import PythonScriptRunner from './client';
import { log } from './logger';


async function main(){
	const runner = new PythonScriptRunner(); 
	const startTime = performance.now();

	const stream = runner.executeScriptStream('main', [
		'--max_pages' , '30', 
		'--max_depth' , '3', 	
		'--url', 'https://grpc.io/docs', 
		'--output_dir' , 'grpc/' ,
		'--name', 'grpc_docs'
	]);

	stream.on('data', (response: any) => {
		if (response.stdout) {
			process.stdout.write(response.stdout);
		}
		if (response.stderr) {
			process.stderr.write(response.stderr);
		}
		if (response.exit_code !== undefined && response.exit_code >= 0) {
			console.log(`\nProcess exited with code ${response.exit_code}`);
		}
	});

	stream.on('error', (err: any) => {
		console.error('gRPC stream error:', err);
	});

	stream.on('end', () => {
		runner.close();
		const duration = performance.now() - startTime;
		log(`Total example.ts (stream) execution time: ${duration.toFixed(0)} ms`);
	});
}

main(); 
