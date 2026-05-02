# Classificador de Suporte com IA

API que classifica tickets de suporte automaticamente por categoria e urgência usando LLM com saída estruturada.

## O problema que resolve
Times de suporte perdem tempo triando tickets manualmente.
Esta API classifica qualquer ticket instantaneamente,
define urgência e sugere resposta profissional.

## Decisões de engenharia

**Saída estruturada com Pydantic**
O LLM retorna JSON validado pelo Pydantic — não texto livre.
Valores fora do schema são rejeitados automaticamente.

**Categorias baseadas em negócio real**
Nota Fiscal, Estoque, Compras, Cadastro — categorias reais
de ERP, não genéricas. Urgência definida por impacto fiscal/operacional.

**Temperature 0.1**
Classificação exige consistência máxima — não criatividade.

## Stack
- FastAPI
- Groq (LLaMA 3.3 70B)
- Pydantic
- Python

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000/docs

## Exemplo de uso

```json
POST /classificar
{
  "titulo": "NF rejeitada pela SEFAZ",
  "descricao": "Erro 539, prazo de entrega hoje"
}

Resposta:
{
  "categoria": "Nota Fiscal",
  "urgencia": "Critica",
  "resumo": "NF rejeitada pela SEFAZ com erro 539 e prazo hoje",
  "resposta_sugerida": "...",
  "confianca": "alta"
}
```

## Próximos passos
- [ ] Integração com sistema de tickets (Jira, Zendesk)
- [ ] Histórico de classificações em banco de dados
- [ ] Dashboard de métricas por categoria
- [ ] Fine-tuning com tickets reais da empresa