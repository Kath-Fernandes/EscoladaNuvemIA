'''Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
'''

ano = int(input('Digite o ano: '))

if ano % 4 == 0: #Se o ano for divisivel por 4, precisa continuar sendo analisado
    if ano % 100 == 0: #Se for divisivel por 100, precisa continuar sendo analisado
        if ano % 400 == 0: #O ano é Bissexto
            print(f'o ano de {ano}, é um ano Bissexto')
        else:
            print(f'O ano de {ano}, não é um ano bissexto')
    else:
        print(f'O ano de {ano}, é um ano bissexto')    
else: 
    print(f'O ano de {ano}, não é um ano bissexto')