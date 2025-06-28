import { performance } from 'perf_hooks';
import PythonScriptRunner from './client';
import { log } from './logger';


async function main(){
	const runner = new PythonScriptRunner(); 
	const startTime = performance.now();
	try{
		// Call the deepcrawl.py script through gRPC. Arguments follow the CLI expected
		// by deepcrawl.py: --url (required) plus optional depth/page limits.
		const result = await runner.executeScript('deepcrawl', [
			'--url', 'https://grpc.io/docs/' 
		]);

		console.log(' exit code : ' , result.exitCode); 
		console.log(' output : ' , result.stdout); 

		if(!result.success){
			console.error(' error : ' , result.stderr);
		}
	}catch(error){
		console.error('grpc error' , error);
	}finally {
		runner.close();
		const duration = performance.now() - startTime;
		log(`Total example.ts execution time: ${duration.toFixed(0)} ms`);
	}
}

main(); 
