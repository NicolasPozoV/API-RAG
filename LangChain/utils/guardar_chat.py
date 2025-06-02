import os
from datetime import datetime

def guardar_conversacion(chat_history, carpeta=None):
    if carpeta is None:
        # Obtén el directorio actual (puede estar en utils/)
        dir_actual = os.path.dirname(os.path.abspath(__file__))
        # Sube un nivel para llegar a LangChain
        langchain_dir = os.path.abspath(os.path.join(dir_actual, ".."))
        # Carpeta conversaciones dentro de LangChain
        carpeta = os.path.join(langchain_dir, "conversaciones")

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    nombre_archivo = datetime.now().strftime("conversacion_%Y%m%d_%H%M%S.txt")
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        for i, (pregunta, respuesta) in enumerate(chat_history, start=1):
            f.write(f"Turno {i}:\n")
            f.write(f"Tú: {pregunta}\n")
            f.write(f"Bot: {respuesta}\n\n")
    
    print(f"Conversación guardada en: {ruta_archivo}")
