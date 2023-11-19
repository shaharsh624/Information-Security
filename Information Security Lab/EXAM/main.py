# Hill Cipher (2)

import numpy as np

# plain_text = input("Enter Plain Text: ").upper()
# keyword = input("Enter Keyword: ").upper()

plain_text = "ACT"
keyword = "GYBNQKURP"
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = len(plain_text)

def encrypt(plain_text, keyword):
    cipher_text = ""
    message_matrix = []
    cipher_matrix = []
    key_matrix = [[0] * n for i in range(n)]
    temp = 0

    # Creating message matrix (P)
    for char in plain_text:
        message_matrix.append([alphabets.index(char)])

    # Creating key matrix (K)
    for i in range(n):
        for j in range(n):
            key_matrix[i][j] = alphabets.index(keyword[temp])
            temp += 1   

    # Creating cipher matrix (C)
    # C = KP mod 26
    result = np.dot(key_matrix, message_matrix)
    cipher_matrix = result % 26

    # Creating cipher text
    for char in cipher_matrix:
        cipher_text += alphabets[int(char[0])]
    
    # print("\nMessage Matrix: \n", message_matrix)
    # print("\nKey Matrix: \n", key_matrix)
    # print("\nCipher Matrix: \n", cipher_matrix)
    return cipher_text

print("\nCipher Text: ", encrypt(plain_text, keyword))