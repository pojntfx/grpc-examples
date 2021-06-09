import os
from concurrent import futures

import grpc

from pymather.proto.mather_pb2_grpc import add_MatherServicer_to_server
from pymather.proto.mather_pb2 import DESCRIPTOR
from pymather.services.mather import Mather
from grpc_reflection.v1alpha import reflection

if __name__ == '__main__':
    laddr = os.getenv("LADDR")
    if not laddr:
        laddr = "0.0.0.0:5000"

    multiplier = os.getenv("MULTIPLIER")
    if not multiplier:
        multiplier = "1"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MatherServicer_to_server(Mather(int(multiplier)), server)

    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['Mather'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(laddr)

    server.start()

    print(f'Listening on {laddr}')

    server.wait_for_termination()
