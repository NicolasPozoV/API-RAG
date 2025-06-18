import logging
from db.mongo import guardar_usuario
from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from utils.chatscript_client import send_to_chatscript
from utils.guardar_chat import guardar_conversacion


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
    respuestas_afirmativas = [
        "sí", "si", "síp", "yes", "por supuesto", "claro", "de acuerdo", "me gustaría", "quiero", "agendar", "cita"
    ]

    try:
        while True:
            query = input("Tú: ")
            if query.lower() in ["salir", "exit", "quit", "adiós", "bye", "hasta luego", "chao", "chau", "terminar", "fin", "cerrar", "salida", "adios"]:
                print("👋 ¡Hasta luego!")
                guardar_conversacion(chat_history)
                break

            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history
            })

            print("Bot (RAG):", respuesta["answer"])
            chat_history.append((query, respuesta["answer"]))

            # Preguntar solo una vez
            if not cita_agendada:
                print("¿Te gustaría agendar una cita para información o consulta?")
                cita_agendada = True

            import re  # al inicio del archivo

            # ...

            if any(palabra in query.lower() for palabra in respuestas_afirmativas) and cita_agendada:
                # Validar nombre
                while not datos_usuario["nombre"]:
                    nombre = input("¿Me indicas tu nombre para agendar? ").strip()
                    if len(nombre) >= 2:
                        datos_usuario["nombre"] = nombre
                    else:
                        print("⚠️ El nombre debe tener al menos 2 caracteres.")

                # Validar teléfono
                while not datos_usuario["telefono"]:
                    telefono = input("¿Y tu número de teléfono? ").strip()
                    if telefono.isdigit() and 7 <= len(telefono) <= 15:
                        datos_usuario["telefono"] = telefono
                    else:
                        print("⚠️ Ingresa un número válido (solo dígitos, entre 7 y 15 caracteres).")

                # Validar correo electrónico
                while not datos_usuario["correo"]:
                    correo = input("¿Cuál es tu correo electrónico? ").strip()
                    if re.match(r"[^@]+@[^@]+\.[^@]+", correo):
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
