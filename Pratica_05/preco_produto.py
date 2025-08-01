'''Crie um programa que receba o preço original de um produto e um percentual de desconto, 
realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto 
(exemplo: 250.75) e o percentual de desconto (exemplo: 10).'''

def calcular_desconto(preco_original , percentual_desconto):
    return (preco_original * percentual_desconto) / 100

#Entrada
preco_original_total = float(input('Digite o valor do produto (em reais): R$ '))
percentual_desconto = float(input('Digite o percentual de desconto a ser aplicado sobre o valor do produto (apenas números): '))

# Calculo
valor_desconto = calcular_desconto(preco_original_total, percentual_desconto)
preco_final = preco_original_total - valor_desconto

# Saida
print(f'O valor do desconto é de R$ {valor_desconto:.2f}, o preço final do produto com desconto é de R$ {preco_final:.2f}')





