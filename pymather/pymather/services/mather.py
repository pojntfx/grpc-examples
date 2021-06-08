from grpclib.server import Server, Stream
from pymather.proto.mather_pb2 import AddInputMessage, AddOutputMessage
from pymather.proto.mather_pb2_grpc import MatherServicer


class Mather(MatherServicer):
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def Add(self, request, context):
        return AddOutputMessage(
            Sum=(request.FirstSummand + request.SecondSummand) *
            self.multiplier)
