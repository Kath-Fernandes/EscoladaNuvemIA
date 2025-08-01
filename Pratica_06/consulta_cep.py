''' Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
 utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado. Verifique se digitou corretamente.")
            return

        logradouro = dados.get("logradouro", "Não disponível")
        bairro = dados.get("bairro", "Não disponível")
        cidade = dados.get("localidade", "Não disponível")
        estado = dados.get("uf", "Não disponível")

        print("\n=== Endereço Encontrado ===")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API ViaCEP: {e}")

def main():
    cep = input("Digite o CEP (somente números): ").strip()

    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Certifique-se de digitar 8 números.")
        return

    consultar_cep(cep)

if __name__ == "__main__":
    main()