import grpc
import concurrent.futures
import example_pb2
import example_pb2_grpc


class ExampleServiceServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        response = example_pb2.Response(message="Hello, " + request.message)
        return response


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
