def build_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    # Remove duplicates from the key and append the alphabet
    key = "".join(dict.fromkeys(key))
    for char in key:
        alphabet = alphabet.replace(char, "")

    # Build the 6x6 Playfair matrix
    matrix = []
    for i in range(0, len(key), 6):
        matrix.append(list(key[i:i + 6]))

    for row in matrix:
        while len(row) < 6:
            row.append(alphabet[0])
            alphabet = alphabet[1:]

    return matrix

def find_char_coordinates(matrix, char):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j


def playfair_decrypt(encrypted_text, key):
    matrix = build_playfair_matrix(key)
    decrypted_text = ""

    # Decrypt the encrypted text
    i = 0
    while i < len(encrypted_text):
        char1 = encrypted_text[i]
        char2 = encrypted_text[i + 1]
        row1, col1 = find_char_coordinates(matrix, char1)
        row2, col2 = find_char_coordinates(matrix, char2)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 6][col1] + matrix[(row2 - 1) % 6][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return decrypted_text

key = "KEYWORD"
encrypted_text = "AFAKCO"

decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
