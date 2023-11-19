# Caesar Cipher - Encryption, Decryption
text = input("Enter some text: ")
key = int(input("Enter key: "))

def encrypt(text, key):
    encrypted_text = ""
    for i in text:
        encrypted_text += chr((ord(i) + key) % 255)
    return encrypted_text

def decrypt(text, key):
    decrypted_text = ""
    for i in text:
        decrypted_text += chr((ord(i) - key) % 255)
    return decrypted_text

print("Encrypted Text: ", encrypt(text, key))
print("Decrypted Text: ", decrypt(encrypt(text, key), key))