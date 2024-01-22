def verificar_paridade(numero):
    # Converte a entrada para inteiro
    numero = int(numero)

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicita ao usuário para inserir um número
numero_usuario = input("Digite um número: ")

# Chama a função e exibe o resultado
resultado = verificar_paridade(numero_usuario)
print(f"{numero_usuario} -> {resultado}")
