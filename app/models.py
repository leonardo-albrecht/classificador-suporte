from pydantic import BaseModel
from typing import Literal

class TicketRequest(BaseModel):
    titulo: str
    descricao: str

class TicketClassificado(BaseModel):
    categoria: Literal["Nota Fiscal", "Estoque", "Compras", "Cadastro","Financeiro",  "Outros"]
    urgencia: Literal["Baixa", "Media", "Alta", "Critica"]
    resumo: str
    resposta_sugerida: str
    confianca: Literal["alta", "media", "baixa"]