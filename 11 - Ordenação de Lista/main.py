numeros = []
while True:
    entrada = input("Digite um número ou 'fim' para terminar: ")
    if entrada == "fim":
        break
    numeros.append(int(entrada))

print(f"Lista original: {numeros}")
numeros_ordenados = sorted(numeros)
print(f"Lista ordenada: {numeros_ordenados}")
