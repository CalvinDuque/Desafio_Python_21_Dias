def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

# Solicita ao usuário que insira o texto
texto_usuario = input("Digite um texto: ")

# Inicializa o contador de palavras
numero_palavras = 0

# Loop for para percorrer cada palavra no texto
for palavra in texto_usuario.split():
    numero_palavras += 1

# Exibe o resultado
print(f'O número de palavras no texto é: {numero_palavras}')
