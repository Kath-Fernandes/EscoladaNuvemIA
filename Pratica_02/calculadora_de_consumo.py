'''Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.'''

#Dados viagem
distancia_percorrida_km = 300
combustivel_gasto_litro = 25

#Calculo médio de consumo (km/l)
consumo_medio = distancia_percorrida_km / combustivel_gasto_litro

#Resultado
print (f'Distância percorrida: {distancia_percorrida_km} km')
print (f'Combustivel gasto: {combustivel_gasto_litro} litros')
print (f'Consumo médio: {consumo_medio:.2f} km/l')