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

def playfair_encrypt(plain_text, key):
    matrix = build_playfair_matrix(key)
    encrypted_text = ""

    # Handle repeating characters by inserting an 'X' between them
    i = 0
    while i < len(plain_text):
        if i == len(plain_text) - 1 or plain_text[i] == plain_text[i + 1]:
            plain_text = plain_text[:i + 1] + 'X' + plain_text[i + 1:]
        i += 2

    # Encrypt the plain text
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1]
        row1, col1 = find_char_coordinates(matrix, char1)
        row2, col2 = find_char_coordinates(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 6][col1] + matrix[(row2 + 1) % 6][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return encrypted_text

key = "KEYWORD"
plaintext = "HELLO"

encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)
