from db.mongo import guardar_usuario
from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from utils.chatscript_client import send_to_chatscript
from utils.guardar_chat import guardar_conversacion
import re  # al inicio del archivo
from utils.validaciones import validar_nombre, validar_telefono, validar_correo
from config.respuestas_afirmativas import RESPUESTAS_AFIRMATIVAS
from config.respuestas_salida import RESPUESTAS_SALIDA

# LangChain/chatbot.py
# Este script implementa un chatbot que utiliza LangChain para responder preguntas
# relacionadas con la empresa Alloxentric, integrando un modelo de lenguaje,

def main():
    user_id = "usuario1"

    # Paso 1: Cargar dependencias RAG
    client = get_client()
    embedding_model = CustomEmbedding()
    vectorstore = create_vectorstore(client, embedding_model)
    llm = load_llm()
    qa_chain = build_qa_chain(llm, vectorstore.as_retriever())

    print("🤖 ChatBot Alloxentric - Escribe 'salir' para terminar.\n")
    chat_history = []

    # Variables para los datos del usuario
    datos_usuario = {
        "nombre": None,
        "correo": None,
        "telefono": None
    }

    cita_agendada = False
    datos_guardados = False  # Bandera para evitar guardar duplicado

    try:
        while True:
            query = input("Tú: ")
            if query.lower() in  RESPUESTAS_SALIDA:
                print("👋 ¡Hasta luego, recuerda ante cualquier duda puedes contactarnos a info@alloxentric.com!")
                guardar_conversacion(chat_history)
                break

            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history
            })

            print("Bot (RAG):", respuesta["answer"])
            chat_history.append((query, respuesta["answer"]))

            # # Preguntar solo una vez
            # if not cita_agendada:
            #     print("¿Te gustaría agendar una cita para información o consulta?")
            #     cita_agendada = True

            # Si la respuesta contiene solo "Lo siento, no tengo información sobre eso", pasamos a agendar
            if "Lo siento, no tengo información sobre eso" in respuesta["answer"]:
                # Si se está preguntando por agendar una cita, el bot debe proceder con el agendamiento
                if any(palabra in query.lower() for palabra in ["sí", "ok", "de acuerdo", "perfecto"]):
                    cita_agendada = True
                    print("¡Perfecto, vamos a agendar tu cita!")

            # Preguntar solo si no se ha preguntado aún por la cita y no se ha dado una respuesta irrelevante
            if not cita_agendada and "Lo siento, no tengo información sobre eso" not in respuesta["answer"]:
                print("¿Te gustaría agendar una cita para información o consulta?")
                cita_agendada = True
        
            # ...

            if any(palabra in query.lower() for palabra in RESPUESTAS_AFIRMATIVAS) and cita_agendada:
                # Validar nombre
                while not datos_usuario["nombre"]:
                    nombre = input("¿Me indica su nombre para agendar? ").strip()
                    if validar_nombre(nombre):
                        datos_usuario["nombre"] = nombre
                    else:
                        print("⚠️ El nombre debe tener al menos 2 caracteres, esto es importante para una agendación correcta.")

                # Validar teléfono
                while not datos_usuario["telefono"]:
                    telefono = input("¿Por favor indíqueme su número de teléfono (+56 9)? ").strip()
                    if validar_telefono(telefono):
                        datos_usuario["telefono"] = telefono
                    else:
                        print("⚠️ Ingresa un número válido (solo dígitos, entre 8 y 15 caracteres).")

                # Validar correo electrónico
                while not datos_usuario["correo"]:
                    correo = input("¿Cuál es su correo electrónico? ").strip()
                    if validar_correo(correo):
                        datos_usuario["correo"] = correo
                    else:
                        print("⚠️ Ingresa un correo electrónico válido (ej: ejemplo@dominio.com).")

                print(f"¡Perfecto, {datos_usuario['nombre']}! Cita agendada con éxito.")
                print(f"Detalles: Nombre: {datos_usuario['nombre']}, Teléfono: {datos_usuario['telefono']}, Correo: {datos_usuario['correo']}")

                if not datos_guardados:
                    guardar_usuario(datos_usuario)
                    datos_guardados = True

    except KeyboardInterrupt:
        print("\n🛑 Interrupción del usuario.")
        guardar_conversacion(chat_history)

    finally:
        client.close()
        if not datos_guardados:
            guardar_usuario(datos_usuario)
        print("🔒 Conexión cerrada y datos guardados.")

if __name__ == "__main__":
    main()
