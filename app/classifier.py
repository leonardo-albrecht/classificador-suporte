from groq import Groq
from dotenv import load_dotenv
from app.models import TicketClassificado
import logging
import json
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """Você é um classificador de tickets de suporte de um sistema ERP empresarial.

Categorias disponíveis:
- Nota Fiscal: problemas com emissão, cancelamento, XML, SEFAZ
- Estoque: divergências, inventário, movimentações, saldo
- Compras: pedidos, fornecedores, cotações, aprovações
- Cadastro: clientes, produtos, fornecedores, usuários
- Outros: qualquer coisa que não se encaixe nas categorias acima

Urgência:
- Critica: Nota Fiscal com prazo fiscal vencendo ou vencido
- Alta: Estoque bloqueado ou divergência crítica
- Media: Compras com pedido parado
- Baixa: Cadastro ou ajustes administrativos

Responda APENAS com JSON válido, sem texto adicional, sem markdown, sem explicações.
Formato exato:
{
  "categoria": "uma das categorias acima",
  "urgencia": "Baixa|Media|Alta|Critica",
  "resumo": "resumo do problema em uma linha",
  "resposta_sugerida": "resposta profissional para o usuário",
  "confianca": "alta|media|baixa"
}"""

def classificar_ticket(titulo: str, descricao: str) -> TicketClassificado:
    prompt = f"Título: {titulo}\nDescrição: {descricao}"
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1
    )
    
    resposta_raw = response.choices[0].message.content
    log.info(f"Tokens usados: {response.usage.total_tokens}")
    log.info(f"Resposta raw: {resposta_raw}")
    
    dados = json.loads(resposta_raw)
    return TicketClassificado(**dados)