// package: pythonservice
// file: service.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";

export class ScriptRequest extends jspb.Message { 
    getScriptName(): string;
    setScriptName(value: string): ScriptRequest;
    clearArgsList(): void;
    getArgsList(): Array<string>;
    setArgsList(value: Array<string>): ScriptRequest;
    addArgs(value: string, index?: number): string;

    getEnvVarsMap(): jspb.Map<string, string>;
    clearEnvVarsMap(): void;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): ScriptRequest.AsObject;
    static toObject(includeInstance: boolean, msg: ScriptRequest): ScriptRequest.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: ScriptRequest, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): ScriptRequest;
    static deserializeBinaryFromReader(message: ScriptRequest, reader: jspb.BinaryReader): ScriptRequest;
}

export namespace ScriptRequest {
    export type AsObject = {
        scriptName: string,
        argsList: Array<string>,

        envVarsMap: Array<[string, string]>,
    }
}

export class ScriptResponse extends jspb.Message { 
    getExitCode(): number;
    setExitCode(value: number): ScriptResponse;
    getStdout(): string;
    setStdout(value: string): ScriptResponse;
    getStderr(): string;
    setStderr(value: string): ScriptResponse;
    getSuccess(): boolean;
    setSuccess(value: boolean): ScriptResponse;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): ScriptResponse.AsObject;
    static toObject(includeInstance: boolean, msg: ScriptResponse): ScriptResponse.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: ScriptResponse, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): ScriptResponse;
    static deserializeBinaryFromReader(message: ScriptResponse, reader: jspb.BinaryReader): ScriptResponse;
}

export namespace ScriptResponse {
    export type AsObject = {
        exitCode: number,
        stdout: string,
        stderr: string,
        success: boolean,
    }
}
