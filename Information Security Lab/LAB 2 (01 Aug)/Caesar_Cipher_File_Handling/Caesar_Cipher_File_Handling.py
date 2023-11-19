
def encrypt():
    with open("Caesar_Cipher_File_Handling/input.txt", 'r') as f :
        text = f.read()
    encrypted_text = ""
    for i in text :
        encrypted_text += chr(ord(i) + 2)
        with open("Caesar_Cipher_File_Handling/encrypted.txt", 'w') as f :
            f.write(encrypted_text)

def decrypt():
    with open("Caesar_Cipher_File_Handling/input.txt", 'r') as f :
        encrypted_text = f.read()
    decrypted_text = ""
    for i in encrypted_text :
        decrypted_text += chr(ord(i) - 2)
    return decrypted_text

print(encrypt())
print(decrypt())