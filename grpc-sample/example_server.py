import grpc
import concurrent.futures
import example_pb2
import example_pb2_grpc


class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        response = example_pb2.Response(message="Hello, " + request.message)
        return response

    def SayHelloClientStream(self, request_iterator, context):
        concatenated_message = ""
        for request in request_iterator:
            concatenated_message += request.message
        response = example_pb2.Response(
            message="Received messages: " + concatenated_message
        )
        return response

    def SayHelloServerStream(self, request, context):
        for _ in range(5):
            yield example_pb2.Response(message="Hello, " + request.message)

    def SayHelloByDicStream(self, request_iterator, context):
        for request in request_iterator:
            yield example_pb2.Response(message="Hello, " + request.message)


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(
        ExampleServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
