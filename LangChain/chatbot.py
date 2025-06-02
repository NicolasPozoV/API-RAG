from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from utils.guardar_chat import guardar_conversacion

def main():
    client = get_client()
    embedding_model = CustomEmbedding()

    vectorstore = create_vectorstore(client, embedding_model)
    llm = load_llm()
    qa_chain = build_qa_chain(llm, vectorstore.as_retriever())

    # print("🤖 ChatBot RAG - Escribe 'salir' para terminar.\n")

    # try:
    #     while True:
    #         query = input("Tú: ")
    #         if query.lower() in ["salir", "exit", "quit"]:
    #             print("Bot: 👋 ¡Hasta luego!")
    #             break

    #         respuesta = qa_chain.invoke({"query": query})
    #         print("Bot:", respuesta["result"])
    # finally:
    #     client.close()

    print("🤖 ChatBot Alloxentric - Escribe 'salir' para terminar.\n")

    chat_history = []

    try:
        while True:
            query = input("Tú: ")
            if query.lower() in ["salir", "exit", "quit"]:
                print("👋 ¡Hasta luego!")
                guardar_conversacion(chat_history)
                break

            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history
            })

            print("Bot:", respuesta["answer"])
            chat_history.append((query, respuesta["answer"]))
    finally:
        client.close()


if __name__ == "__main__":
    main()

