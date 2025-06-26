import os
from datetime import datetime

def guardar_conversacion(chat_history, carpeta=None, id_conversacion=None):
    if carpeta is None:
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        langchain_dir = os.path.abspath(os.path.join(dir_actual, ".."))
        carpeta = os.path.join(langchain_dir, "conversaciones")

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Usa el ID si se proporciona, si no crea uno nuevo
    nombre_archivo = f"{id_conversacion or datetime.now().strftime('conversacion_%Y%m%d_%H%M%S')}.txt"
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        for i, (pregunta, respuesta) in enumerate(chat_history, start=1):
            f.write(f"Turno {i}:\n")
            f.write(f"Tú: {pregunta}\n")
            f.write(f"Bot: {respuesta}\n\n")

    print(f"Conversación guardada en: {ruta_archivo}")
