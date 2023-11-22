def caesar_cipher_encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            is_uppercase = char.isupper()
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if is_uppercase else "abcdefghijklmnopqrstuvwxyz"
            key_id = (alphabet.index(char) + key) % 26
            encrypted_text += alphabet[key_id]
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, key):
    return caesar_cipher_encrypt(ciphertext, -key)

def caesar_cipher_brute_force_attack(ciphertext):
    decrypted_results = []
    for key in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, key)
        decrypted_results.append((key, decrypted_text))
    return decrypted_results

def caesar_cipher_frequency_analysis(ciphertext):
    frequencies = {}
    for char in ciphertext:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_frequencies

# Example usage:
plaintext = "My name is Adit!"
key = 3

# Encryption
encrypted_text = caesar_cipher_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

# Brute-force attack
ciphertext = "Pb qdph lv Dglw!"
decrypted_results = caesar_cipher_brute_force_attack(ciphertext)
for key, decrypted_text in decrypted_results:
    print(f"Key: {key}, Decrypted text: {decrypted_text}")

# Frequency analysis
ciphertext = "Qc reqi mw Ehmx!"
frequencies = caesar_cipher_frequency_analysis(ciphertext)
print("Character frequencies in the ciphertext:", frequencies)
