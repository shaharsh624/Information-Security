# text = input("Enter your text: ")
text = "Meet me at 2pm in cafe"

def encryption(text):
    no_of_words = len(text.split())
    splitted_text = text.split()
    added_words = 0
    if (no_of_words % 2) != 0:
        splitted_text.append("-1")
        no_of_words += 1
        added_words += 1
    for i in range(0, no_of_words, 2) :
        temp = splitted_text[i]
        splitted_text[i] = splitted_text[i+1]
        splitted_text[i+1] = temp
    encrypted_text = splitted_text + [str(no_of_words - added_words)]

    return ' '.join(map(str,encrypted_text))


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


def decryption(text):
    encrypted_text = text.split()
    no_of_words = int(encrypted_text[-1])
    del encrypted_text[-1]
    added_words = 0
    if (no_of_words % 2) != 0:
        no_of_words += 1
        added_words += 1

    for i in range(0, no_of_words, 2) :
        temp = encrypted_text[i]
        encrypted_text[i] = encrypted_text[i+1]
        encrypted_text[i+1] = temp
    if (added_words == 1):
        del encrypted_text[-1]
    return ' '.join(map(str,encrypted_text))

print(decryption(decryption_ascii(encryption_ascii(encryption(text)))))
