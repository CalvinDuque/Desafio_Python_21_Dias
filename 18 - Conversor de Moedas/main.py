import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f'https://open.er-api.com/v6/latest/{moeda_origem}'
    response = requests.get(url)
    if response.status_code != 200:
        print('Erro ao obter taxa de conversão.')
        return
    taxa = response.json()['rates'][moeda_destino]
    valor_convertido = valor * taxa
    print(f'{valor:.2f} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}')

while True:
    valor = float(input('Digite o valor a ser convertido: '))
    moeda_origem = input('Digite a moeda de origem: ').upper()
    moeda_destino = input('Digite a moeda de destino: ').upper()
    converter_moeda(valor, moeda_origem, moeda_destino)
    opcao = input('Deseja fazer outra conversão? (S/N) ').upper()
    if opcao == 'N':
        break
