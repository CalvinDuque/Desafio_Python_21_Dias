def eh_palindromo(texto):
    # Remover espaços e converter para minúsculas
    texto_formatado = ''.join(texto.lower().split())

    # Verificar se a string é igual à sua reversa
    return texto_formatado == texto_formatado[::-1]


# Solicitar entrada do usuário
entrada_usuario = input("Digite uma palavra ou frase: ")

# Verificar se é um palíndromo e exibir o resultado
if eh_palindromo(entrada_usuario):
    print(f"{entrada_usuario} é um palíndromo!")
else:
    print(f"{entrada_usuario} não é um palíndromo.")