def playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = []

    for _ in range(6):
        row = [''] * 6
        matrix.append(row)

    key_id = 0
    alpha_id = 0

    for row in range(6):
        for column in range(6):
            if key_id < len(key):
                matrix[row][column] = key[key_id]
                key_id += 1
            else:
                while alphabet[alpha_id] in key:
                    alpha_id += 1
                matrix[row][column] = alphabet[alpha_id]
                alpha_id += 1
    return matrix

def position(matrix, char):
    for row in range(6):
        for column in range(6):
            if matrix[row][column] == char:
                return row, column

def encrypt(plaintext, key):
    matrix = playfair_matrix(key)
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ""
    i = 0

    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = ""

        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]

        if char1 == char2:
            char2 = 'X'
            i = i + 1

        row1, column1 = position(matrix, char1)
        row2, column2 = position(matrix, char2)

        if row1 == row2:
            column1 = (column1 + 1) % 6
            column2 = (column2 + 1) % 6
        elif column1 == column2:
            row1 = (row1 + 1) % 6
            row2 = (row2 + 1) % 6
        else:
            column1, column2 = column2, column1

        ciphertext += matrix[row1][column1] + matrix[row2][column2]
        i = i + 2
    return ciphertext

def decrypt(ciphertext, key):
    matrix = playfair_matrix(key)
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    i = 0

    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ""

        if i + 1 < len(ciphertext):
            char2 = ciphertext[i + 1]

        row1, column1 = position(matrix, char1)
        row2, column2 = position(matrix, char2)

        if row1 == row2:
            column1 = (column1 - 1) % 6
            column2 = (column2 - 1) % 6
        elif column1 == column2:
            row1 = (row1 - 1) % 6
            row2 = (row2 - 1) % 6
        else:
            column1, column2 = column2, column1

        plaintext += matrix[row1][column1] + matrix[row2][column2]
        i = i + 2
    return plaintext


key = "PLAYFAIRCIPHER"
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

ciphertext = encrypt(plaintext, key)
print("Encrypted Ciphertext: ", ciphertext)

plain_text = decrypt(ciphertext, key)
print("Decrypted Plaintext: ", plain_text)
