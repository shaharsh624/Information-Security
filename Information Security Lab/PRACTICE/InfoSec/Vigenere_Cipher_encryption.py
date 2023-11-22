def vigenere_encrypt(plaintext, key):
    ciphertext = ""

    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % len(key)].upper()
            shift = ord(key_char) - ord('A')

            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))

            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext


plaintext = "Kohli goes down the ground! Kohli goes out of the ground! A magnificent strike into the crowd!"
key = "Test"

ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)
