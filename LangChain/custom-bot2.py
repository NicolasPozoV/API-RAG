from langchain_weaviate import WeaviateVectorStore
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import weaviate
import os

# Cargar variables de entorno
load_dotenv()

# Embedding con wrapper
class CustomEmbedding:
    def __init__(self, model):
        self.model = model

    def embed_query(self, text):
        return self.model.encode(text).tolist()

model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = CustomEmbedding(model)

# Cliente local
client = weaviate.connect_to_local(port=8080, grpc_port=50051)

# Vector store
vectorstore = WeaviateVectorStore(
    client=client,
    index_name="PdfPage",
    text_key="content",
    embedding=embedding,
)

# LLM desde Groq
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0,
)

# QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Consulta
query = "¿Qué dice el PDF sobre el cliente?"
respuesta = qa_chain.invoke(query)  # ← usando invoke, no run

print(respuesta)

client.close()
