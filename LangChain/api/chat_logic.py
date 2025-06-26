# api/chat_logic.py

from datetime import datetime
import json
from chains.qa_chains import build_qa_chain
from chains.extraction import build_extractor_chain
from config.respuestas_salida import RESPUESTAS_SALIDA
from utils.json import extraer_json_del_texto
from db.mongo import guardar_usuario
from utils.guardar_chat import guardar_conversacion
from retriever.vector_store import create_vectorstore
from retriever.weaviate_client import get_client
from embeddings.embedding_model import CustomEmbedding
from llm.groq_model import load_llm

client = get_client()
embedding_model = CustomEmbedding()
vectorstore = create_vectorstore(client, embedding_model)
llm = load_llm()

qa_chain = build_qa_chain(llm, vectorstore.as_retriever())
extractor_chain = build_extractor_chain(llm)

def procesar_chat_simple(query, chat_history, id_conversacion=None):
    if not id_conversacion:
        id_conversacion = datetime.now().strftime("conversacion_%Y%m%d_%H%M%S")

    chat_history.append((query, ""))

    resultado = extractor_chain.invoke({"chat_history": str(chat_history)})
    json_str = extraer_json_del_texto(resultado.content)

    datos_usuario = {
        "nombre": None, "empresa": None, "necesidad": None,
        "correo": None, "idioma": None, "agenda": None,
        "id_conversacion": id_conversacion
    }

    if json_str:
        try:
            extraidos = json.loads(json_str)
            for key in datos_usuario:
                if key != "id_conversacion" and extraidos.get(key):
                    datos_usuario[key] = extraidos[key]
        except json.JSONDecodeError:
            pass

    resumen_usuario = f"""
        Idioma: {datos_usuario['idioma'] or 'No proporcionado'}
        Nombre: {datos_usuario['nombre'] or 'No proporcionado'}
        Correo: {datos_usuario['correo'] or 'No proporcionado'}
        Empresa: {datos_usuario['empresa'] or 'No proporcionado'}
        Necesidad: {datos_usuario['necesidad'] or 'No proporcionado'}
        Agenda: {datos_usuario['agenda'] or 'No proporcionado'}
    """.strip()

    respuesta = qa_chain.invoke({
        "question": query,
        "chat_history": chat_history,
        "user_data": resumen_usuario
    })

    chat_history[-1] = (query, respuesta["answer"])

    if all(v for k, v in datos_usuario.items() if k != "id_conversacion"):
        guardar_usuario(datos_usuario)
        guardar_conversacion(chat_history, id_conversacion=id_conversacion)

    return {
        "respuesta": respuesta["answer"],
        "id_conversacion": id_conversacion
    }
