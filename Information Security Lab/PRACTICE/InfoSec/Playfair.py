def generate_key_square(key):
    # Create a key square with the given key
    key = key.replace(" ", "").upper()
    key_square = ""
    for char in key:
        if char not in key_square:
            key_square += char
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789":
        if char not in key_square:
            key_square += char
    return key_square

def encrypt(plaintext, key):
    # Encrypt the plaintext using the Playfair cipher with the given key
    key_square = generate_key_square(key)
    ciphertext = ""
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")
    if len(plaintext) % 2 == 1:
        plaintext += "X"
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1]
        a_row, a_col = divmod(key_square.index(a), 6)
        b_row, b_col = divmod(key_square.index(b), 6)
        if a_row == b_row:
            a_col = (a_col + 1) % 6
            b_col = (b_col + 1) % 6
        elif a_col == b_col:
            a_row = (a_row + 1) % 6
            b_row = (b_row + 1) % 6
        else:
            a_col, b_col = b_col, a_col
        ciphertext += key_square[a_row*6+a_col]
        ciphertext += key_square[b_row*6+b_col]
    return ciphertext

def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the Playfair cipher with the given key
    key_square = generate_key_square(key)
    plaintext = ""
    ciphertext = ciphertext.upper().replace(" ", "").replace("J", "I")
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1]
        a_row, a_col = divmod(key_square.index(a), 6)
        b_row, b_col = divmod(key_square.index(b), 6)
        if a_row == b_row:
            a_col = (a_col - 1) % 6
            b_col = (b_col - 1) % 6
        elif a_col == b_col:
            a_row = (a_row - 1) % 6
            b_row = (b_row - 1) % 6
        else:
            a_col, b_col = b_col, a_col
        plaintext += key_square[a_row*6+a_col]
        plaintext += key_square[b_row*6+b_col]
    return plaintext


plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
key = "PLAYFAIRCIPHER"
key_square = generate_key_square(key)
print("Key matrix:")
for i in range(0, 36, 6):
    print(" ".join(key_square[i:i+6]))
print()
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)


