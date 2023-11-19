# Finding the key
ciphertext = input("Enter some ciphertext: ")
text = input("Enter the original text to verify: ")

for key in range(-25, 26):
    decrypted_text = ""
    for i in ciphertext:
        decrypted_text += chr(ord(i) - key)
    print(decrypted_text)
    if decrypted_text == text:
        print("Key:", key)
        break