// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('@grpc/grpc-js');
var proto_mather_pb = require('../proto/mather_pb.js');

function serialize_com_pojtinger_felix_grpcExamples_gomather_AddInputMessage(arg) {
  if (!(arg instanceof proto_mather_pb.AddInputMessage)) {
    throw new Error('Expected argument of type com.pojtinger.felix.grpcExamples.gomather.AddInputMessage');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_com_pojtinger_felix_grpcExamples_gomather_AddInputMessage(buffer_arg) {
  return proto_mather_pb.AddInputMessage.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_com_pojtinger_felix_grpcExamples_gomather_AddOutputMessage(arg) {
  if (!(arg instanceof proto_mather_pb.AddOutputMessage)) {
    throw new Error('Expected argument of type com.pojtinger.felix.grpcExamples.gomather.AddOutputMessage');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_com_pojtinger_felix_grpcExamples_gomather_AddOutputMessage(buffer_arg) {
  return proto_mather_pb.AddOutputMessage.deserializeBinary(new Uint8Array(buffer_arg));
}


var MatherService = exports.MatherService = {
  add: {
    path: '/com.pojtinger.felix.grpcExamples.gomather.Mather/Add',
    requestStream: false,
    responseStream: false,
    requestType: proto_mather_pb.AddInputMessage,
    responseType: proto_mather_pb.AddOutputMessage,
    requestSerialize: serialize_com_pojtinger_felix_grpcExamples_gomather_AddInputMessage,
    requestDeserialize: deserialize_com_pojtinger_felix_grpcExamples_gomather_AddInputMessage,
    responseSerialize: serialize_com_pojtinger_felix_grpcExamples_gomather_AddOutputMessage,
    responseDeserialize: deserialize_com_pojtinger_felix_grpcExamples_gomather_AddOutputMessage,
  },
};

exports.MatherClient = grpc.makeGenericClientConstructor(MatherService);
