import logging
from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from utils.chatscript_client import send_to_chatscript
from utils.guardar_chat import guardar_conversacion

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chat_debug.log"),  # También guarda en archivo
        logging.StreamHandler()  # Y lo muestra en consola
    ]
)

def main():
    user_id = "usuario1"  # puedes cambiarlo dinámicamente si es multiusuario

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
                guardar_conversacion(chat_history)
                break

            # # Paso 2: Intentar primero con ChatScript
            # cs_response = send_to_chatscript(user_id, query)
            # print(">> llega a ChatScript")

            # if cs_response and cs_response != "__NO_MATCH__":
            #     logging.info(f"[ChatScript] Query: {query} | Response: {cs_response}")
            #     print("Bot (ChatScript):", cs_response)
            #     chat_history.append((query, cs_response))
            #     continue

            # Paso 3: Si ChatScript no responde, usar RAG
            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history
            })

            logging.info(f"[RAG] Query: {query} | Response: {respuesta['answer']}")
            print("Bot (RAG):", respuesta["answer"])
            chat_history.append((query, respuesta["answer"]))

    except KeyboardInterrupt:
        print("\n🛑 Interrupción del usuario.")
        guardar_conversacion(chat_history)

    finally:
        client.close()


if __name__ == "__main__":
    main()
