'''
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

nome_produto = 'Camiseta'
preco_original = 50.00
porcentagem_desconto = 20

#Valor desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

#Resultado final
preco_desconto = preco_original - valor_desconto

print ('Produto:', nome_produto)
print (f'Preço Original: R$ {preco_original: .2f}')
print (f'Preço com desconto de {porcentagem_desconto}%: R$ {preco_desconto: .2f}')
