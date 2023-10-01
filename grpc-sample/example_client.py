import grpc
import example_pb2
import example_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = example_pb2_grpc.ExampleServiceStub(channel)

    # Unary RPC (SayHello)
    request_unary = example_pb2.Request(message="World")
    response_unary = stub.SayHello(request_unary)
    print("Response received from server (Unary RPC): " + response_unary.message)

    # Client Streaming RPC (SayHelloClientStream)
    client_stream_messages = ["Hello", " from", " client", " stream"]
    client_stream_request_iterator = (
        example_pb2.Request(message=message) for message in client_stream_messages
    )
    response_client_stream = stub.SayHelloClientStream(client_stream_request_iterator)
    print(
        "Response received from server (Client Streaming RPC): "
        + response_client_stream.message
    )

    # Server Streaming RPC (SayHelloServerStream)
    server_stream_request = example_pb2.Request(message="Server Stream")
    server_stream_responses = stub.SayHelloServerStream(server_stream_request)
    print("Responses received from server (Server Streaming RPC):")
    for response in server_stream_responses:
        print(response.message)

    # Bidirectional Streaming RPC (SayHelloByDicStream)
    bidirectional_stream_messages = [
        "Hello",
        " from",
        " client",
        " bidirectional",
        " stream",
    ]
    bidirectional_stream_request_iterator = (
        example_pb2.Request(message=message)
        for message in bidirectional_stream_messages
    )
    bidirectional_stream_responses = stub.SayHelloByDicStream(
        bidirectional_stream_request_iterator
    )
    print("Responses received from server (Bidirectional Streaming RPC):")
    for response in bidirectional_stream_responses:
        print(response.message)


if __name__ == "__main__":
    run()
