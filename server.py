#!/usr/bin/env python

import os
import grpc
import sys
import asyncio
import traceback

from tempfile import TemporaryDirectory
from concurrent.futures import ProcessPoolExecutor as Pool
from crewgen.proto import crewgenerator_pb2 as pb2
from crewgen.proto import crewgenerator_pb2_grpc as pb2_grpc
from grpc_reflection.v1alpha import reflection

PYTHON = sys.executable
WORKERPATH = os.path.realpath(os.path.join(os.path.dirname(__file__), 'worker.py'))

class CrewGeneratorServicer(pb2_grpc.CrewGeneratorServicer):
    async def GenerateHtmlGame(self, request, _context):
        try:
            description = request.description
            with TemporaryDirectory() as tmpdir:
                process = await asyncio.create_subprocess_exec(
                    PYTHON, WORKERPATH, description, stdout=sys.stdout, stderr=sys.stderr, cwd=tmpdir)

                await process.communicate()
                with open(os.path.join(tmpdir, 'game.html'), 'rb') as f:
                    data = f.read()

                response = pb2.GenerateHtmlGameResponse(html=pb2.FileResponse(data=data))
            return response
        except Exception as e:
            traceback.print_exc()
            raise e


async def serve(address):
    server = grpc.aio.server()
    pb2_grpc.add_CrewGeneratorServicer_to_server(CrewGeneratorServicer(),
                                                 server)

    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['CrewGenerator'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port(address)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    print('Serving on 0.0.0.0:9452', file=sys.stderr)
    asyncio.run(serve('0.0.0.0:9452'))
