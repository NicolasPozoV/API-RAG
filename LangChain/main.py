from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple, Optional
from api.chat_logic import procesar_chat_simple

app = FastAPI()

class ChatRequest(BaseModel):
    question: str
    chat_history: List[Tuple[str, str]]
    id_conversacion: Optional[str] = None

@app.post("/chat")
def chat(request: ChatRequest):
    return procesar_chat_simple(
        query=request.question,
        chat_history=request.chat_history,
        id_conversacion=request.id_conversacion
    )
