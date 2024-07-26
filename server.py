#!/usr/bin/env python

import grpc
import sys

from concurrent import futures
from crewgen.proto import crewgenerator_pb2 as pb2
from crewgen.proto import crewgenerator_pb2_grpc as pb2_grpc
from grpc_reflection.v1alpha import reflection

import worker


class CrewGeneratorServicer(pb2_grpc.CrewGeneratorServicer):
    def GenerateHtmlGame(self, request, _context):
        description = request.description
        data = worker.generate_game_html(description)
        response = pb2.GenerateHtmlGameResponse(html=pb2.FileResponse(data=data))
        return response


def serve(address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CrewGeneratorServicer_to_server(CrewGeneratorServicer(),
                                                 server)

    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['CrewGenerator'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(address)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    print('Serving on [::]:9452', file=sys.stderr)
    serve('[::]:9452')
