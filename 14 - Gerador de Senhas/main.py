import random
import string

def generate_password(length, uppercase, lowercase, digits, symbols):
    # Define the character sets to use for each type of character
    uppercase_chars = string.ascii_uppercase if uppercase else ''
    lowercase_chars = string.ascii_lowercase if lowercase else ''
    digit_chars = string.digits if digits else ''
    symbol_chars = string.punctuation if symbols else ''

    # Combine the character sets into a single set of characters
    all_chars = uppercase_chars + lowercase_chars + digit_chars + symbol_chars

    # Generate a password by randomly selecting characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Example usage
length = int(input("Digite o comprimento da senha: "))
uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
digits = input("Incluir números? (s/n): ").lower() == 's'
symbols = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

password = generate_password(length, uppercase, lowercase, digits, symbols)
print("Senha gerada:", password)
