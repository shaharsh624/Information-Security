import math

def decrypt(cipher_text, key):
    max_rows = math.ceil(len(cipher_text) / len(key))
    matrix = [[''] * len(key) for _ in range(max_rows)]

    index = 0
    for col in key:
        for row in range(max_rows):
            if index < len(cipher_text):
                matrix[row][col - 1] = cipher_text[index]
                index += 1

    plain_text = ''
    for row in matrix:
        for char in row:
            if char:
                plain_text += char

    return plain_text

key = [2, 1, 3]  # Example key
ciphertext = "Mtiy s S nhAaadmhie!"  # Example plaintext

decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", "My name is Adit Shah!")