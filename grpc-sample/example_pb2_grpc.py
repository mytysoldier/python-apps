# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2


class ExampleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/ExampleService/SayHello',
                request_serializer=example__pb2.Request.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )
        self.SayHelloClientStream = channel.stream_unary(
                '/ExampleService/SayHelloClientStream',
                request_serializer=example__pb2.Request.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )
        self.SayHelloServerStream = channel.unary_stream(
                '/ExampleService/SayHelloServerStream',
                request_serializer=example__pb2.Request.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )
        self.SayHelloByDicStream = channel.stream_stream(
                '/ExampleService/SayHelloByDicStream',
                request_serializer=example__pb2.Request.SerializeToString,
                response_deserializer=example__pb2.Response.FromString,
                )


class ExampleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloClientStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloServerStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloByDicStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=example__pb2.Request.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
            'SayHelloClientStream': grpc.stream_unary_rpc_method_handler(
                    servicer.SayHelloClientStream,
                    request_deserializer=example__pb2.Request.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
            'SayHelloServerStream': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloServerStream,
                    request_deserializer=example__pb2.Request.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
            'SayHelloByDicStream': grpc.stream_stream_rpc_method_handler(
                    servicer.SayHelloByDicStream,
                    request_deserializer=example__pb2.Request.FromString,
                    response_serializer=example__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ExampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExampleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ExampleService/SayHello',
            example__pb2.Request.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloClientStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/ExampleService/SayHelloClientStream',
            example__pb2.Request.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloServerStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ExampleService/SayHelloServerStream',
            example__pb2.Request.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloByDicStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/ExampleService/SayHelloByDicStream',
            example__pb2.Request.SerializeToString,
            example__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
