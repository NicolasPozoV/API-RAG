from pymongo import MongoClient

# Conexión al servidor local
client = MongoClient("mongodb://localhost:27017/")
db = client["alloxentric"]
coleccion = db["usuarios"]

def guardar_usuario(datos_usuario: dict):
    if datos_usuario["nombre"] and datos_usuario["correo"] and datos_usuario["empresa"] and datos_usuario["necesidad"]:
        resultado = coleccion.insert_one(datos_usuario)
        print(f"✅ Datos del usuario guardados en MongoDB con _id: {resultado.inserted_id}")
    else:
        print("⚠️ No se guardó en MongoDB: faltan datos.")
