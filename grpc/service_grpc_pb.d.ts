// package: pythonservice
// file: service.proto

/* tslint:disable */
/* eslint-disable */

import * as grpc from "@grpc/grpc-js";
import * as service_pb from "./service_pb";

interface IPythonRunnerService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
    executeScript: IPythonRunnerService_IExecuteScript;
    executeScriptStream: IPythonRunnerService_IExecuteScriptStream;
}

interface IPythonRunnerService_IExecuteScript extends grpc.MethodDefinition<service_pb.ScriptRequest, service_pb.ScriptResponse> {
    path: "/pythonservice.PythonRunner/ExecuteScript";
    requestStream: false;
    responseStream: false;
    requestSerialize: grpc.serialize<service_pb.ScriptRequest>;
    requestDeserialize: grpc.deserialize<service_pb.ScriptRequest>;
    responseSerialize: grpc.serialize<service_pb.ScriptResponse>;
    responseDeserialize: grpc.deserialize<service_pb.ScriptResponse>;
}
interface IPythonRunnerService_IExecuteScriptStream extends grpc.MethodDefinition<service_pb.ScriptRequest, service_pb.ScriptResponse> {
    path: "/pythonservice.PythonRunner/ExecuteScriptStream";
    requestStream: false;
    responseStream: true;
    requestSerialize: grpc.serialize<service_pb.ScriptRequest>;
    requestDeserialize: grpc.deserialize<service_pb.ScriptRequest>;
    responseSerialize: grpc.serialize<service_pb.ScriptResponse>;
    responseDeserialize: grpc.deserialize<service_pb.ScriptResponse>;
}

export const PythonRunnerService: IPythonRunnerService;

export interface IPythonRunnerServer extends grpc.UntypedServiceImplementation {
    executeScript: grpc.handleUnaryCall<service_pb.ScriptRequest, service_pb.ScriptResponse>;
    executeScriptStream: grpc.handleServerStreamingCall<service_pb.ScriptRequest, service_pb.ScriptResponse>;
}

export interface IPythonRunnerClient {
    executeScript(request: service_pb.ScriptRequest, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    executeScript(request: service_pb.ScriptRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    executeScript(request: service_pb.ScriptRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    executeScriptStream(request: service_pb.ScriptRequest, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<service_pb.ScriptResponse>;
    executeScriptStream(request: service_pb.ScriptRequest, metadata?: grpc.Metadata, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<service_pb.ScriptResponse>;
}

export class PythonRunnerClient extends grpc.Client implements IPythonRunnerClient {
    constructor(address: string, credentials: grpc.ChannelCredentials, options?: Partial<grpc.ClientOptions>);
    public executeScript(request: service_pb.ScriptRequest, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    public executeScript(request: service_pb.ScriptRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    public executeScript(request: service_pb.ScriptRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: service_pb.ScriptResponse) => void): grpc.ClientUnaryCall;
    public executeScriptStream(request: service_pb.ScriptRequest, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<service_pb.ScriptResponse>;
    public executeScriptStream(request: service_pb.ScriptRequest, metadata?: grpc.Metadata, options?: Partial<grpc.CallOptions>): grpc.ClientReadableStream<service_pb.ScriptResponse>;
}
