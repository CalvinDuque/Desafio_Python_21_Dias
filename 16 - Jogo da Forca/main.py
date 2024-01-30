import random

def escolher_palavra():
    palavras = ['gato', 'cachorro', 'elefante', 'girafa', 'leão']
    return random.choice(palavras)

def ocultar_palavra(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def jogar():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 0
    max_tentativas = 6

    while tentativas < max_tentativas:
        print(ocultar_palavra(palavra, letras_corretas))
        letra = input('Digite uma letra: ')
        if letra in letras_corretas:
            print('Você já tentou essa letra antes!')
        elif letra in palavra:
            letras_corretas.add(letra)
            if set(palavra) == letras_corretas:
                print('Parabéns, você ganhou!')
                break
        else:
            tentativas += 1
            print('Essa letra não está na palavra. Tentativas restantes:', max_tentativas - tentativas)

    if tentativas == max_tentativas:
        print('Você perdeu! A palavra era:', palavra)

jogar()
