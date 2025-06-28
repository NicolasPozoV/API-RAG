from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from api.chat_logic import procesar_chat_simple

app = FastAPI()

# ✅ Habilitar CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a dominios específicos si lo deseas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    input: str  # <-- antes era "question"
    id_conversacion: Optional[str] = None

@app.post("/chat")
def chat(request: ChatRequest):
    return procesar_chat_simple(
        query=request.input,
        id_conversacion=request.id_conversacion
    )
