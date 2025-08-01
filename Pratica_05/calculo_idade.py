'''Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.'''

from datetime import datetime

def idade_em_dias_completa(dia, mes, ano):
    data_nascimento = datetime(ano, mes, dia)
    data_atual = datetime.now()
    idade_dias = (data_atual - data_nascimento).days
    return idade_dias

# Exemplo de uso:
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))
ano = int(input("Digite o ano do nascimento: "))

dias = idade_em_dias_completa(dia, mes, ano)
print(f"Sua idade exata em dias é: {dias} dias")