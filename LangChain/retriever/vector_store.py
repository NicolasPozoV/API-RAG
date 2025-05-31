from langchain_weaviate import WeaviateVectorStore

def create_vectorstore(client, embedding):
    return WeaviateVectorStore(
        client=client,
        index_name="PdfPage",
        text_key="content",
        embedding=embedding,
    )
