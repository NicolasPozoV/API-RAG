# cleaner.py
from pymongo import MongoClient
from datetime import datetime, timedelta

# Conexión Mongo
client = MongoClient("mongodb://localhost:27017/")
db = client["alloxentric"]
coleccion_activas = db["conversaciones"]
coleccion_finalizadas = db["finalizadas"]

# Tiempo de inactividad máximo
LIMITE_MINUTOS = 30

now = datetime.utcnow()
limite = now - timedelta(minutes=LIMITE_MINUTOS)

# Buscar documentos inactivos (estimando inactividad desde la última modificación)
inactivas = coleccion_activas.find({
    "ultima_modificacion": {"$lte": limite}
})

print(f"🔍 Encontradas {inactivas.count()} conversaciones inactivas para mover...")

for doc in inactivas:
    id_conversacion = doc["id_conversacion"]
    doc["movido_en"] = now
    coleccion_finalizadas.insert_one(doc)
    coleccion_activas.delete_one({"_id": doc["_id"]})
    print(f"✅ Movida a finalizadas: {id_conversacion}")

print("🧹 Limpieza completada.")
