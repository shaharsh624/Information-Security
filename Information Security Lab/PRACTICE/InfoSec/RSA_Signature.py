import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Modular inverse does not exist")


# Function to sign a message with the sender's private key
def sign_message(message, e, n):
    message_bytes = message.encode()
    message_int = int.from_bytes(message_bytes, byteorder="big")
    signature = pow(message_int, e, n)
    return signature


# Function to verify the signature of a message using the sender's public key
def verify_signature(message, signature, d, n):
    message_bytes = message.encode()
    message_int = int.from_bytes(message_bytes, byteorder="big")
    decrypted_signature = pow(signature, d, n)
    return message_int == decrypted_signature


# Generate two prime numbers for the RSA key pair
p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

while p == q:
    q = generate_prime(1000, 5000)

n = p * q
phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

print("Public Key (e):", e)
print("Private Key (d):", d)
print("n:", n)
print("Phi of n:", phi_n)
print("p:", p)
print("q:", q)

# Sender's Authentication
message_to_sign = "Sender is authentic"
signature = sign_message(message_to_sign, e, n)
print("Message to sign:", message_to_sign)
print("Signature:", signature)
is_authentic = verify_signature(message_to_sign, signature, d, n)
print("Is sender authentic?", is_authentic)

# Message Confidentiality
plaintext = "Hello, this is a confidential message."
plaintext_encryption = [ord(ch) for ch in plaintext]
ciphertext = [pow(ch, e, n) for ch in plaintext_encryption]
ciphertext_alphabet = [chr((ch % 26) + 65) for ch in ciphertext]
plaintext_decryption = [pow(ch, d, n) for ch in ciphertext]
decrypted_text = "".join(chr(ch) for ch in plaintext_decryption)
print("Original Message:", plaintext)
print("Ciphertext:", "".join(ciphertext_alphabet))
print("Decrypted Message:", decrypted_text)
