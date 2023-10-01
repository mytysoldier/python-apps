import grpc
import example_pb2
import example_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = example_pb2_grpc.ExampleServiceStub(channel)
    request = example_pb2.Request(message="World")
    response = stub.SayHello(request)
    print("Response received from server: " + response.message)


if __name__ == "__main__":
    run()
