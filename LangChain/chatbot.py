from db.mongo import guardar_usuario
from embeddings.embedding_model import CustomEmbedding
from retriever.weaviate_client import get_client
from retriever.vector_store import create_vectorstore
from llm.groq_model import load_llm
from chains.qa_chains import build_qa_chain
from chains.extraction import build_extractor_chain
from utils.guardar_chat import guardar_conversacion
from config.respuestas_salida import RESPUESTAS_SALIDA
from utils.json import extraer_json_del_texto
import json
from colorama import init, Fore, Style

init(autoreset=True)



def main():
    client = get_client()
    embedding_model = CustomEmbedding()
    vectorstore = create_vectorstore(client, embedding_model)
    llm = load_llm()

    qa_chain = build_qa_chain(llm, vectorstore.as_retriever())
    extractor_chain = build_extractor_chain(llm)

    print(Fore.CYAN + "🤖 ChatBot Alloxentric - Escribe 'salir' para terminar.\n")

    chat_history = []
    datos_usuario = {"nombre": None, "empresa": None, "necesidad": None, "correo": None, "idioma": None , "agenda": None}
    datos_guardados = False

    try:
        while True:
            query = input(Fore.GREEN + "Tú: " + Style.RESET_ALL)
            if query.lower() in RESPUESTAS_SALIDA:
                print(Fore.CYAN + "👋 ¡Hasta luego, recuerda ante cualquier duda puedes contactarnos a info@alloxentric.com!")
                guardar_conversacion(chat_history)
                break

            # 1. Agregar input provisional (respuesta vacía por ahora)
            chat_history.append((query, ""))

            # 2. Extraer datos del usuario antes de responder
            resultado = extractor_chain.invoke({"chat_history": str(chat_history)})
            json_str = extraer_json_del_texto(resultado.content)

            if json_str:
                try:
                    extraidos = json.loads(json_str)
                    for key in datos_usuario:
                        if not datos_usuario[key] and extraidos.get(key):
                            datos_usuario[key] = extraidos[key]
                except json.JSONDecodeError:
                    pass

            # 3. Crear resumen con los datos ya extraídos
            resumen_usuario = f"""
                Idioma: {datos_usuario['idioma'] or 'No proporcionado'}
                Nombre: {datos_usuario['nombre'] or 'No proporcionado'}
                Correo: {datos_usuario['correo'] or 'No proporcionado'}
                Empresa: {datos_usuario['empresa'] or 'No proporcionado'}
                Necesidad: {datos_usuario['necesidad'] or 'No proporcionado'}
                Agenda: {datos_usuario['agenda'] or 'No proporcionado'}
                """.strip()

            # 4. Obtener respuesta del bot usando el resumen actualizado
            respuesta = qa_chain.invoke({
                "question": query,
                "chat_history": chat_history,
                "user_data": resumen_usuario
            })

            # 5. Actualizar historial con la respuesta real
            chat_history[-1] = (query, respuesta["answer"])
            print(Fore.YELLOW + "Bot (RAG):", respuesta["answer"])

            # 6. Guardar los datos si ya están completos
            if all(datos_usuario.values()) and not datos_guardados:
                guardar_usuario(datos_usuario)
                print(Fore.MAGENTA + "✅ Datos del usuario guardados correctamente.")
                datos_guardados = True

    except KeyboardInterrupt:
        print(Fore.RED + "\n🛑 Interrupción del usuario.")
        guardar_conversacion(chat_history)

    finally:
        client.close()
        if all(datos_usuario.values()) and not datos_guardados:
            guardar_usuario(datos_usuario)
        print(Fore.CYAN + "🔒 Conexión cerrada y datos guardados.")
        print(Fore.BLUE + "Datos guardados:", datos_usuario)

if __name__ == "__main__":
    main()
