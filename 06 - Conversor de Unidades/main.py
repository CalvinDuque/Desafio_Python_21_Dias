print("Bem-vindo ao conversor de unidades!")
print("Por favor, escolha uma opção:")
print("1 - Quilômetros para Milhas")
print("2 - Milhas para Quilômetros")
print("3 - Metros para Pés")
print("4 - Pés para Metros")
print("5 - Graus Celsius para Fahrenheit")
print("6 - Graus Fahrenheit para Celsius")

opcao = input("Digite o número da opção desejada: ")

if opcao not in ["1", "2", "3", "4", "5", "6"]:
    print("Opção inválida.")
else:
    valor = float(input("Digite o valor a ser convertido: "))

    if opcao == "1":
        resultado = valor * 0.621371
        print(f"{valor} quilômetros = {resultado} milhas")
    elif opcao == "2":
        resultado = valor * 1.60934
        print(f"{valor} milhas = {resultado} quilômetros")
    elif opcao == "3":
        resultado = valor * 3.28084
        print(f"{valor} metros = {resultado} pés")
    elif opcao == "4":
        resultado = valor * 0.3048
        print(f"{valor} pés = {resultado} metros")
    elif opcao == "5":
        resultado = (valor * 9/5) + 32
        print(f"{valor} graus Celsius = {resultado} graus Fahrenheit")
    elif opcao == "6":
        resultado = (valor - 32) * 5/9
        print(f"{valor} graus Fahrenheit = {resultado} graus Celsius")
