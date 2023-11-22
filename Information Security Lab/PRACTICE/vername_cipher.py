def encrypt(plaintext, key):
    cipher = ""
    for p, k in zip(plaintext, key):
        dec1 = ord(p) - 65
        dec2 = ord(k) - 65
        ans = dec1 ^ dec2
        cipher += chr((ans % 26) + 65)
    return cipher


plaintext = "OAK"
key = "SON"

print("Plaintext:", plaintext)
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
