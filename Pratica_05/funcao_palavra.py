'''Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

import unicodedata

def remover_acentos(texto: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn')

def is_palindromo(texto: str) -> bool:
    texto_sem_acentos = remover_acentos(texto)
    texto_limpo = ''.join(char.lower() for char in texto_sem_acentos if char.isalnum())
    return texto_limpo == texto_limpo[::-1]

while True:
    entrada = input("Digite uma palavra ou frase (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        print("Programa encerrado.")
        break

    if is_palindromo(entrada):
        print("É palíndromo? Sim\n")
    else:
        print("É palíndromo? Não\n")