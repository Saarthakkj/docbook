// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var service_pb = require('./service_pb.js');

function serialize_pythonservice_ScriptRequest(arg) {
  if (!(arg instanceof service_pb.ScriptRequest)) {
    throw new Error('Expected argument of type pythonservice.ScriptRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_pythonservice_ScriptRequest(buffer_arg) {
  return service_pb.ScriptRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_pythonservice_ScriptResponse(arg) {
  if (!(arg instanceof service_pb.ScriptResponse)) {
    throw new Error('Expected argument of type pythonservice.ScriptResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_pythonservice_ScriptResponse(buffer_arg) {
  return service_pb.ScriptResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var PythonRunnerService = exports.PythonRunnerService = {
  executeScript: {
    path: '/pythonservice.PythonRunner/ExecuteScript',
    requestStream: false,
    responseStream: false,
    requestType: service_pb.ScriptRequest,
    responseType: service_pb.ScriptResponse,
    requestSerialize: serialize_pythonservice_ScriptRequest,
    requestDeserialize: deserialize_pythonservice_ScriptRequest,
    responseSerialize: serialize_pythonservice_ScriptResponse,
    responseDeserialize: deserialize_pythonservice_ScriptResponse,
  },
  executeScriptStream: {
    path: '/pythonservice.PythonRunner/ExecuteScriptStream',
    requestStream: false,
    responseStream: true,
    requestType: service_pb.ScriptRequest,
    responseType: service_pb.ScriptResponse,
    requestSerialize: serialize_pythonservice_ScriptRequest,
    requestDeserialize: deserialize_pythonservice_ScriptRequest,
    responseSerialize: serialize_pythonservice_ScriptResponse,
    responseDeserialize: deserialize_pythonservice_ScriptResponse,
  },
};

exports.PythonRunnerClient = grpc.makeGenericClientConstructor(PythonRunnerService, 'PythonRunner');
