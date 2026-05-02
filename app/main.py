from fastapi import FastAPI, HTTPException
from app.models import TicketRequest, TicketClassificado
from app.classifier import classificar_ticket
import logging

log = logging.getLogger(__name__)

app = FastAPI(
    title="Classificador de Suporte com IA",
    description="Classifica tickets de suporte por categoria e urgência automaticamente",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/classificar", response_model=TicketClassificado)
def classificar(ticket: TicketRequest):
    try:
        resultado = classificar_ticket(ticket.titulo, ticket.descricao)
        return resultado
    except Exception as e:
        log.error(f"Erro ao classificar ticket: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))