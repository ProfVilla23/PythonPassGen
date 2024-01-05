import random
import string

symbol = 0
lower = 0
upper = 0
number = 0
password = []

length = input("Bienvenido al generador de contraseñas, ¿cuántos caracteres quieres que tenga tu contraseña? (mínimo 8): \n ")
length = 128 if length == '' else int(length)

character_types = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

for _ in range(length):
    selected_type = random.choice(character_types)
    if selected_type == string.ascii_lowercase:
        lower += 1
        password.append(random.choice(string.ascii_lowercase))
    elif selected_type == string.ascii_uppercase:
        upper += 1
        password.append(random.choice(string.ascii_uppercase))
    elif selected_type == string.digits:
        number += 1
        password.append(random.choice(string.digits))
    elif selected_type == string.punctuation:
        symbol += 1
        password.append(random.choice(string.punctuation))

word = "".join(password)
print(f"\nTu contraseña de tamaño {length} es: ")
print('******')
print(word)
print('******')
print(f"\nContiene {lower} minúsculas, {upper} mayúsculas, {number} números y {symbol} caracteres especiales")
input('Password copied to clipboard, push a button to exit...')
