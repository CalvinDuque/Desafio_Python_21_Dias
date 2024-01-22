def analisar_frequencia(texto):
    # Inicializa um dicionário para armazenar a frequência de cada letra
    frequencia_letras = {}

    # Itera sobre cada caractere no texto
    for letra in texto:
        # Verifica se o caractere é uma letra
        if letra.isalpha():
            # Converte a letra para minúscula para evitar diferenciação entre maiúsculas e minúsculas
            letra = letra.lower()

            # Atualiza a contagem da letra no dicionário de frequência
            frequencia_letras[letra] = frequencia_letras.get(letra, 0) + 1

    return frequencia_letras

# Solicita ao usuário para fornecer o texto
texto_usuario = input("Digite o texto: ")

# Chama a função e exibe o resultado
resultado = analisar_frequencia(texto_usuario)
print("Resultado:")
print(resultado)
