'''Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:
A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
'''
while True:
    # Primeiro número
    num1 = input("Digite o primeiro número: ")
    try:
        num1 = float(num1)
    except:
        print("Erro: número inválido.")
        continue

    # Segundo número
    num2 = input("Digite o segundo número: ")
    try:
        num2 = float(num2)
    except:
        print("Erro: número inválido.")
        continue

    # Operação
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: não é possível dividir por zero.")
            continue
        resultado = num1 / num2
    else:
        print("Erro: operação inválida. Use apenas +, -, * ou /.")
        continue

    # Resultado final
    print(f"Resultado: {num1} {operacao} {num2} = {resultado:.2f}")
    break