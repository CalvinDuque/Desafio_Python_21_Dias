contatos = []

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    contato = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def listar_contatos():
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, E-mail: {contato['email']}")
            return
    print("Contato não encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print("Contato excluído com sucesso!")
            return
    print("Contato não encontrado.")

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Excluir contato")
    print("5 - Sair")
    opcao = input("Opção escolhida: ")
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        buscar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")