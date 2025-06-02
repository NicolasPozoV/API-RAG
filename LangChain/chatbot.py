from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from utils.chatscript_client import send_to_chatscript


def main():
    #user_id = null

    # Paso 1: Cargar dependencias RAG
    client = get_client()
    embedding_model = CustomEmbedding()
    vectorstore = create_vectorstore(client, embedding_model)
    llm = load_llm()
    qa_chain = build_qa_chain(llm, vectorstore.as_retriever())
    print("🤖 ChatBot Alloxentric - Escribe 'salir' para terminar.\n")

    chat_history = []

    try:
        while True:
            query = input("Tú: ")
            if query.lower() in ["salir", "exit", "quit"]:
                print("👋 ¡Hasta luego!")
                break

            # Paso 2: Intentar primero con ChatScript
           # cs_response = send_to_chatscript(user_id, query)

            #if cs_response and not cs_response.lower().startswith("unknown"):
             #   print("Bot (ChatScript):", cs_response)
              #  chat_history.append((query, cs_response))
               # continue

            # Paso 3: Si ChatScript no responde, usar RAG
            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history
            })

            print("Bot (RAG):", respuesta["answer"])
            chat_history.append((query, respuesta["answer"]))

    finally:
        client.close()


if __name__ == "__main__":
    main()