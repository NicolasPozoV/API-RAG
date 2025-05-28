from langchain_weaviate import WeaviateVectorStore
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

connection_params = ConnectionParams.from_url(
    "http://localhost:8080",
    grpc_port=8081
)

client = WeaviateClient(connection_params=connection_params)
client.connect()  # <--- conecta explícitamente


embedding = OllamaEmbeddings(model="llama3")  # Usando Ollama para embeddings locales

vectorstore = WeaviateVectorStore(
    client=client,
    index_name="PdfPage",
    text_key="content",
    embedding=embedding,
)

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

query = "¿Qué dice el PDF sobre el cliente?"
respuesta = qa_chain.run(query)

print(respuesta)
