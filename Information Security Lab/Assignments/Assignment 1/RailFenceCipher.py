def encrypt(plaintext, key):
    matrix = [['' for _ in range(len(plaintext))] for _ in range(key)]
    row = 0
    step = 1

    for i in range(len(plaintext)):
        matrix[row][i] = plaintext[i]
        row += step

        if row == 0 or row == key - 1:
            step = -step

    ciphertext = ''
    for i in range(key):
        for j in range(len(plaintext)):
            if matrix[i][j] != '':
                ciphertext += matrix[i][j]

    return ciphertext


def decrypt(ciphertext, key):
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(key)]
    row = 0
    step = 1

    for i in range(len(ciphertext)):
        matrix[row][i] = '*'
        row += step

        if row == 0 or row == key - 1:
            step = -step

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*' and index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    plaintext = ''
    row = 0
    step = 1

    for i in range(len(ciphertext)):
        plaintext += matrix[row][i]
        row += step

        if row == 0 or row == key - 1:
            step = -step

    return plaintext


def main():
    key = int(input("Enter Encryption Key: "))
    input_string = input("Enter Input String: ")

    encrypted_text = encrypt(input_string, key)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
