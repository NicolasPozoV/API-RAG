# db/mongo.py
from pymongo import MongoClient
from datetime import datetime

# Conexión al servidor local
client = MongoClient("mongodb://localhost:27017/")
db = client["alloxentric"]
coleccion_usuarios = db["usuarios"]
coleccion_conversaciones = db["conversaciones"]
coleccion_finalizadas = db["finalizadas"]  # Asegúrate de tenerla creada

def guardar_usuario(datos_usuario: dict):
    if datos_usuario["nombre"] and datos_usuario["correo"] and datos_usuario["empresa"] and datos_usuario["necesidad"]:
        resultado = coleccion_usuarios.insert_one(datos_usuario)
        print(f"✅ Datos del usuario guardados en MongoDB con _id: {resultado.inserted_id}")
    else:
        print("⚠️ No se guardó en MongoDB: faltan datos.")

def cargar_conversacion(id_conversacion: str):
    doc = coleccion_conversaciones.find_one({"id_conversacion": id_conversacion})
    if doc:
        historial = doc.get("historial", [])
        return [tuple(turno) for turno in historial]
    return []

def guardar_conversacion(historial: list, id_conversacion: str):
    historial_serializable = [list(turno) for turno in historial]
    coleccion_conversaciones.update_one(
        {"id_conversacion": id_conversacion},
        {"$set": {
            "historial": historial_serializable,
            "ultima_modificacion": datetime.utcnow()
        }},
        upsert=True
    )
    print(f"💾 Conversación guardada en Mongo con ID: {id_conversacion}")

def mover_a_finalizadas(id_conversacion: str):
    doc = coleccion_conversaciones.find_one({"id_conversacion": id_conversacion})
    if doc:
        coleccion_finalizadas.insert_one(doc)
        coleccion_conversaciones.delete_one({"id_conversacion": id_conversacion})
        print(f"📦 Conversación {id_conversacion} movida a finalizadas")
