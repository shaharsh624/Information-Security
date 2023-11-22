def additive_cipher(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            index = ord(char.upper()) - ord("A")
            cipher_index = (index + key) % 26
            cipher_char = chr(cipher_index + ord("A"))
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext


def multiplicative_cipher(plaintext, key):
    ciphertext = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            index = ord(char.upper()) - ord("A")
            if (i + 1) % 2 == 0:  # Even index
                cipher_index = (index * key) % 26
            else:  # Odd index
                cipher_index = (index + key) % 26
            cipher_char = chr(cipher_index + ord("A"))
            ciphertext += cipher_char
        else:
            ciphertext += char
    return ciphertext


def encrypt_message():
    plaintext = input("Enter the plaintext: ").upper()
    key = int(input("Enter the key: "))

    additive_result = additive_cipher(plaintext, key)
    multiplicative_result = multiplicative_cipher(plaintext, key)

    ciphertext = ""
    for i, char in enumerate(plaintext):
        if i % 2 == 0:  # Odd index
            ciphertext += additive_result[i]
        else:  # Even index
            ciphertext += multiplicative_result[i]

    print(f"Ciphertext: {ciphertext}")


encrypt_message()
