'''Crie um programa que solicite a idade do usuário e classifique-oem uma das seguintes categorias:
Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais).
'''

def classificar_idade(idade):
    if idade < 0:
        return "Idade inválida."
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

# Entrada
try:
    idade = int(input("Digite sua idade: "))
    classificacao = classificar_idade(idade)
    print(f"Classificação: {classificacao}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")