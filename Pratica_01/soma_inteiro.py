"""
5- Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D. 
Fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros.
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

numero_a = int(input("Informe o valor de A: "))
numero_b = int(input("Informe o valor de B: "))
numero_c = int(input("Informe o valor de C: "))
numero_d = int(input("Informe o valor de D: "))

diferenca = (numero_a * numero_b) - (numero_c * numero_d)
print(f"A Diferença é {diferenca}")