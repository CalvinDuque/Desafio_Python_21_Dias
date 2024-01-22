import random

# Função que verifica se um número é primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função que executa o jogo
def play_game():
    score = 0
    while True:
        num = random.randint(1, 100)
        guess = input("O número " + str(num) + " é primo? (s/n) ")
        if guess.lower() == "s" and is_prime(num):
            score += 1
            print("Correto! Sua pontuação agora é", score)
        elif guess.lower() == "n" and not is_prime(num):
            score += 1
            print("Correto! Sua pontuação agora é", score)
        else:
            print("Incorreto. A resposta correta era", "sim" if is_prime(num) else "não")
            print("Sua pontuação final foi", score)
            break

# Função que exibe a pontuação atual
def show_score():
    print("Sua pontuação atual é", score)

# Função que reseta a pontuação
def reset_score():
    score = 0
    print("Pontuação resetada para 0")

# Loop principal do jogo
while True:
    choice = input("Digite 1 para jogar, 2 para ver sua pontuação, 3 para resetar sua pontuação ou 4 para sair: ")
    if choice == "1":
        play_game()
    elif choice == "2":
        show_score()
    elif choice == "3":
        reset_score()
    elif choice == "4":
        break
    else:
        print("Escolha inválida. Por favor, digite 1, 2, 3 ou 4.")
