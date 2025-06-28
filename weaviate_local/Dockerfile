# Imagen base con Python
FROM python:3.11

# Actualizar paquetes del sistema para reducir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Crear directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script y PDFs
COPY load_pdfs.py .
COPY PDF/ ./PDF/

# Ejecutar el script al iniciar
CMD ["python", "load_pdfs.py"]
