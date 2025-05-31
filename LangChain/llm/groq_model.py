# from langchain_groq import ChatGroq
# from config.settings import GROQ_API_KEY

# def load_llm():
#     return ChatGroq(
#         api_key=GROQ_API_KEY,
#         model="llama-3.1-8b-instant",
#         temperature=0,
#     )

from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

def load_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        temperature=0.0,
    )
