import re

def is_valid_email(email):
    # Define a regular expression pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Compile the pattern into a regular expression object
    regex = re.compile(pattern)

    # Use the regular expression object to match the email string
    match = regex.match(email)

    # Return True if the email string matches the pattern, False otherwise
    return bool(match)

# Example usage
email = input("Digite o endereço de e-mail: ")
if is_valid_email(email):
    print("O endereço de e-mail é válido.")
else:
    print("O endereço de e-mail é inválido.")
