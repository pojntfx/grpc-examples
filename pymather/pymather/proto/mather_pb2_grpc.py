# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pymather.proto import mather_pb2 as pymather_dot_proto_dot_mather__pb2


class MatherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Add = channel.unary_unary(
                '/com.pojtinger.felix.grpcExamples.gomather.Mather/Add',
                request_serializer=pymather_dot_proto_dot_mather__pb2.AddInputMessage.SerializeToString,
                response_deserializer=pymather_dot_proto_dot_mather__pb2.AddOutputMessage.FromString,
                )


class MatherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MatherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Add': grpc.unary_unary_rpc_method_handler(
                    servicer.Add,
                    request_deserializer=pymather_dot_proto_dot_mather__pb2.AddInputMessage.FromString,
                    response_serializer=pymather_dot_proto_dot_mather__pb2.AddOutputMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.pojtinger.felix.grpcExamples.gomather.Mather', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mather(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.pojtinger.felix.grpcExamples.gomather.Mather/Add',
            pymather_dot_proto_dot_mather__pb2.AddInputMessage.SerializeToString,
            pymather_dot_proto_dot_mather__pb2.AddOutputMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
