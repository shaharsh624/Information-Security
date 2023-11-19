import numpy as np

plain_text = "ACT"
keyword = "GYBNQKURP"
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIZE = 3


def modulus_mul(A, M):
    for X in range(1, M):
        if ((A % M) * (X % M)) % M == 1:
            return X
    return -1


def inverse_matrix(matrix):
    det = np.linalg.det(matrix)
    inv = np.linalg.inv(matrix)

    mul_inv = modulus_mul(int(det), 26)
    inv = (det * inv) % 26
    inv = (mul_inv * inv) % 26

    return inv


def encrypt(plain_text, keyword):
    cipher_text = ""
    message_matrix = []
    cipher_matrix = []
    key_matrix = [[0] * SIZE for i in range(SIZE)]
    temp = 0
    for char in plain_text:
        message_matrix.append([alphabets.index(char)])

    for i in range(SIZE):
        for j in range(SIZE):
            key_matrix[i][j] = alphabets.index(keyword[temp])
            temp += 1

    result = np.dot(key_matrix, message_matrix)
    cipher_matrix = result % 26

    for char in cipher_matrix:
        cipher_text += alphabets[int(char[0])]
    return cipher_text


def decrypt(cipher_text, keyword):
    cipher_matrix = []
    plain_text = ""
    key_matrix = [[0] * SIZE for i in range(SIZE)]
    temp = 0
    for char in cipher_text:
        cipher_matrix.append([alphabets.index(char)])

    for i in range(SIZE):
        for j in range(SIZE):
            key_matrix[i][j] = alphabets.index(keyword[temp])
            temp += 1

    key_matrix = inverse_matrix(key_matrix)  # Inverse of key matrix
    key_matrix = key_matrix % 26
    result = np.dot(key_matrix, cipher_matrix)
    result = np.rint(result).astype(int) % 26

    for char in result:
        plain_text += alphabets[int(char[0])]
    return plain_text


cipher_text = encrypt(plain_text, keyword)
print("Cipher text (Encrypted):", cipher_text)
print("Plain Text (Decrypted):", decrypt(cipher_text, keyword))
