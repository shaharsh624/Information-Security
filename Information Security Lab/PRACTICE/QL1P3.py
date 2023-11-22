def func(plain_text, filler, key):
    key_length = len(str(key))
    text_length = len(plain_text)
    key_str = str(key)
    fillers = ""
    cipher_text = ""

    if text_length % key_length != 0:
        # Add filler
        rem_length = key_length - (text_length % key_length)
        fillers = filler * rem_length
        plain_text += fillers
    
    for i, p in enumerate(plain_text):
        cipher_text += chr(((ord(p)-65 + int(key_str[i%key_length]))%26)+65)
    return cipher_text

def find_filler(plain_text):
    plain_ord = [ord(i) for i in plain_text]
    minimum=min(plain_ord)
    return(chr(minimum))
        

# plain_text = input("Enter your message: ")
# filler = input("Enter min_letter: ")
# key = input("Enter key: ")

plain_text = "GRONSFELD"
filler = find_filler(plain_text)
key = 1234

print(func(plain_text, filler, key))
