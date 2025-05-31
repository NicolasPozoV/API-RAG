import weaviate

def get_client():
    return weaviate.connect_to_local(port=8080, grpc_port=50051)
