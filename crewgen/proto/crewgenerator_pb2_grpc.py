# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crewgen.proto import crewgenerator_pb2 as crewgen_dot_proto_dot_crewgenerator__pb2


class CrewGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateHtmlGame = channel.unary_unary(
                '/crewgen.CrewGenerator/GenerateHtmlGame',
                request_serializer=crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameRequest.SerializeToString,
                response_deserializer=crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameResponse.FromString,
                )


class CrewGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateHtmlGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CrewGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateHtmlGame': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateHtmlGame,
                    request_deserializer=crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameRequest.FromString,
                    response_serializer=crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'crewgen.CrewGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CrewGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateHtmlGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/crewgen.CrewGenerator/GenerateHtmlGame',
            crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameRequest.SerializeToString,
            crewgen_dot_proto_dot_crewgenerator__pb2.GenerateHtmlGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
