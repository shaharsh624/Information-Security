def vigenere_decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % len(key)].upper()
            shift = ord(key_char) - ord('A')

            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))

            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


ciphertext = "Dszeb yhxw whaf mlw zvgngh! Dszeb yhxw hnx hy lax ykhyfw! S feygbjavxrl lxjbdi bgxg mlw vvgpw!"
key = "Test"

plaintext = vigenere_decrypt(ciphertext, key)
print("Plaintext: ", plaintext)
