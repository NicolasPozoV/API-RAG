# 🧠 Sistema de QA con LangChain, Weaviate y Groq

Este proyecto permite realizar preguntas sobre documentos cargados en una base vectorial usando:

* [LangChain](https://www.langchain.com/)
* [Weaviate](https://weaviate.io/) (base vectorial local)
* [Groq](https://groq.com/) (modelo LLM rápido y económico)
* [SentenceTransformers](https://www.sbert.net/) (para embeddings)

---

## ⚙️ Requisitos Previos

### 🐍 Python

* Python 3.8 o superior.

### 🧠 Weaviate (local)

Debes tener **Weaviate corriendo de forma local**, ya sea con Docker o instalado directamente.

#### Opción 1: Usando Docker

```bash
docker run -d \
  -p 8080:8080 \
  -p 50051:50051 \
  --name weaviate \
  semitechnologies/weaviate:latest \
  --host 0.0.0.0 \
  --port 8080 \
  --grpc-port 50051 \
  --persistency.data.path="/var/lib/weaviate" \
  --enable-module=text2vec-contextionary \
  --module-config='{"text2vec-contextionary": {"vectorizeClassName": "false"}}' \
  --default-vectorizer=none
```

> Asegúrate de que Weaviate esté corriendo en `http://localhost:8080` antes de ejecutar el script.

### 🔑 Clave API de Groq

Crea un archivo `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_clave_api_de_groq
```

Puedes conseguir una clave en [https://console.groq.com](https://console.groq.com).

---

## 📦 Instalación de Dependencias

Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 📄 Descripción del Código

```python
# 1. Cargar variables de entorno
load_dotenv()

# 2. Definir clase custom para embeddings con SentenceTransformer
# 3. Conectar a cliente Weaviate local (puertos 8080 / 50051)
# 4. Crear VectorStore con LangChain y Weaviate
# 5. Cargar modelo LLM desde Groq (llama-3.1-8b-instant)
# 6. Crear cadena de QA con RetrievalQA
# 7. Hacer pregunta e imprimir respuesta
# 8. Cerrar cliente al final
```

---

## 🧪 Ejemplo de uso

```bash
python main.py
```

Salida esperada:

```
{'result': 'El nombre de la empresa es Alloxentric'}
```

---

## 🧹 Tips

* Asegúrate de que la clase `PdfPage` ya exista en Weaviate con los documentos vectorizados. Si no, este script **no va a funcionar**.
* Puedes cargar datos a Weaviate usando un script previo de ingesta o directamente desde la consola de administración de Weaviate.

---

## 🛑 Cierre de conexión

Al finalizar, el cliente de Weaviate se cierra automáticamente:

```python
client.close()
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Sientete libre de usar, modificar y compartir.
