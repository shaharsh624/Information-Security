text = input("Enter your text: ")

def encryption_ascii(text):
    encrypted_text = ""
    for i in text :
        encrypted_text += str(chr(ord(i)+12))
    return encrypted_text

def decryption_ascii(encrypted_text):
    decrypted_text = ""
    for i in encrypted_text :
        decrypted_text += str(chr(ord(i)-12))
    return decrypted_text

print(encryption_ascii(text))
print(decryption_ascii(encryption_ascii(text)))
