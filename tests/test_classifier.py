import pytest
from app.classifier import classificar_ticket

def test_nota_fiscal_critica():
    resultado = classificar_ticket(
        titulo="NF rejeitada pela SEFAZ",
        descricao="Nota fiscal com erro 539, prazo de entrega vence hoje"
    )
    assert resultado.categoria == "Nota Fiscal"
    assert resultado.urgencia == "Critica"

def test_compras_media():
    resultado = classificar_ticket(
        titulo="Pedido de compra parado",
        descricao="Pedido de compra número 1052 está parado há 2 dias sem aprovação"
    )
    assert resultado.categoria == "Compras"
    assert resultado.urgencia == "Media"

def test_cadastro_baixa():
    resultado = classificar_ticket(
        titulo="Cadastro de novo usuário",
        descricao="Precisamos cadastrar um novo usuário no sistema para a próxima semana"
    )
    assert resultado.categoria == "Cadastro"
    assert resultado.urgencia == "Baixa"

def test_nota_fiscal_nao_e_cadastro():
    resultado = classificar_ticket(
        titulo="NF rejeitada pela SEFAZ",
        descricao="Nota fiscal com erro 539, prazo de entrega vence hoje"
    )
    assert resultado.categoria != "Cadastro"
    assert resultado.urgencia != "Baixa"

def test_contas_a_receber():
    resultado = classificar_ticket(
        titulo="Financeiro contas a receber",
        descricao="Contas a receber com erro, prazo de entrega hoje"
    )
    assert resultado.categoria == "Financeiro"
    assert resultado.urgencia == "Critica"