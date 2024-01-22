import random

numero_secreto = random.randint(1, 100)
tentativas_restantes = 7

print("Bem-vindo ao jogo de adivinhação!")
print("O programa gerou um número aleatório entre 1 e 100.")
print("Você tem 7 tentativas para adivinhar o número correto.")

while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}")
    chute = int(input("Digite um número: "))

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior do que o seu chute.")
    else:
        print("O número secreto é menor do que o seu chute.")

    tentativas_restantes -= 1

if tentativas_restantes == 0:
    print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
