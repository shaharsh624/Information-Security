def keyword_extend(key, n):
    key_original = key
    key_length = len(key)
    for i in range(n - key_length):
        key += key_original[i % key_length]
    return key


def find_alphabet(index):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabets[index]


def find_index(character):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabets.index(character)


def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += find_alphabet(
            (find_index(plaintext[i]) + find_index(keyword[i])) % 26
        )
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += find_alphabet(
            (find_index(ciphertext[i]) - find_index(keyword[i])) % 26
        )
    return plaintext


if __name__ == "__main__":
    plaintext = input("Enter some plaintext: ")
    key = input("Enter the keyword: ")

    plaintext = plaintext.replace(" ", "").upper()
    key = key.replace(" ", "").upper()

    entended_key = keyword_extend(key, len(plaintext))

    cipher_text = encrypt_vigenere(plaintext.upper(), entended_key.upper())
    print("Cipher Text (encrypted): ", cipher_text)

    plain_text = decrypt_vigenere(cipher_text.upper(), entended_key.upper())
    print("Plain Text (decrypted): ", plain_text)
