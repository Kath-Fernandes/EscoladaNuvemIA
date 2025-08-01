''' Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O
 usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
 além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.'''

import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada. Verifique o código informado.")
            return

        info = dados[chave]
        nome = info.get("name", "N/A")
        valor_atual = info.get("bid", "N/A")
        valor_maximo = info.get("high", "N/A")
        valor_minimo = info.get("low", "N/A")
        ultima_atualizacao = info.get("create_date", "N/A")

        print(f"\n=== Cotação de {nome} ===")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Valor máximo: R$ {valor_maximo}")
        print(f"Valor mínimo: R$ {valor_minimo}")
        print(f"Última atualização: {ultima_atualizacao}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")

def main():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()

    if not moeda.isalpha() or len(moeda) != 3:
        print("Código inválido. Use apenas letras (ex: USD).")
        return

    consultar_cotacao(moeda)

if __name__ == "__main__":
    main()