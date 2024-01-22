print("Bem-vindo à calculadora básica!")
print("Por favor, escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Digite o número da operação desejada: ")

if operacao not in ["1", "2", "3", "4"]:
    print("Operação inválida.")
else:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == "2":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == "3":
        resultado = num1 * num2
        print(f"{num1} x {num2} = {resultado}")
    elif operacao == "4":
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
