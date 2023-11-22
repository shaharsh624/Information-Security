import math


def decrypt(cipher_text, key):
    max_rows = math.ceil(len(cipher_text) / len(key))
    matrix = [[""] * len(key) for _ in range(max_rows)]

    index = 0
    for col in key:
        for row in range(max_rows):
            if index < len(cipher_text):
                matrix[row][col - 1] = cipher_text[index]
                index += 1

    plain_text = ""
    for row in matrix:
        for char in row:
            if char:
                plain_text += char

    return plain_text


def encrypt(plain_text, key):
    num_columns = len(key)
    num_rows = -(-len(plain_text) // num_columns)

    matrix = [[""] * num_columns for _ in range(num_rows)]

    index = 0
    for col in key:
        for row in range(num_rows):
            if index < len(plain_text):
                matrix[row][col - 1] = plain_text[index]
                index += 1

    cipher_text = ""
    for row in matrix:
        for char in row:
            if char:
                cipher_text += char

    return cipher_text


key = [2, 1, 3]
plain_text = "My name is Adit Shah!"

encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
# print("Decrypted text:", "My name is Adit Shah!")
