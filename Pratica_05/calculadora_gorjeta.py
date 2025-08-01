'''Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return (valor_conta * porcentagem_gorjeta) / 100

# Entrada Parâmetros
valor_total_conta = float(input('Digite o valor total da conta (em reais): R$ '))
porcentagem_gorjeta = float(input('Digite a porcentagem da gorjeta desejada (somente número): '))

# Cálculo
gorjeta_calculada = calcular_gorjeta(valor_total_conta, porcentagem_gorjeta)

# Retorno
print(f'O valor total da gorjeta calculada é de: R$ {gorjeta_calculada:.2f}')

