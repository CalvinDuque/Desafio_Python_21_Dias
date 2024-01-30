import csv

# Cria um arquivo CSV vazio para armazenar os detalhes dos livros
with open('biblioteca.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Título', 'Autor', 'Ano de Publicação'])

# Função para adicionar um novo livro à biblioteca
def adicionar_livro():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o nome do autor: ')
    ano = input('Digite o ano de publicação: ')

    # Adiciona o novo livro ao arquivo CSV
    with open('biblioteca.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, autor, ano])

    print('Livro adicionado com sucesso!')

# Função para listar todos os livros na biblioteca
def listar_livros():
    # Lê os dados do arquivo CSV
    with open('biblioteca.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Menu de opções para o usuário
while True:
    print('Selecione uma opção:')
    print('1. Adicionar um novo livro')
    print('2. Listar todos os livros')
    print('3. Sair')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        break
    else:
        print('Opção inválida. Tente novamente.')
