# text = input("Enter your text: ")
text = "Meet me at 2pm in coffee shop"


def encryption(text):
    no_of_words = len(text.split())
    splitted_text = text.split()
    added_words = 0
    if (no_of_words % 2) != 0:
        splitted_text.append(" ")
        no_of_words += 1
        added_words += 1
    for i in range(0, no_of_words, 2) :
        temp = splitted_text[i]
        splitted_text[i] = splitted_text[i+1]
        splitted_text[i+1] = temp
    encrypted_text = splitted_text + [no_of_words - added_words]
    return encrypted_text

# ['me', 'Meet', '2pm', 'at', 'coffee', 'at', ' ', 'shop', 7]

def decryption(encrypted_text):
    no_of_words = encrypted_text[-1]
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
    return encrypted_text

print(encryption(text))
print(decryption(encryption(text)))
