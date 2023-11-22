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
        if (d*e)%phi == 1:
            return d
    raise ValueError("mod inverse does not exist")

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

while p==q:
    q = generate_prime(1000, 5000)

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)


d = mod_inverse(e, phi_n)

print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p: ", p)
print("q:  ", q)


plaintext = "Hello World, How are You?"

plaintext_encryption = [ord(ch) for ch in plaintext]
# (m ^ e)mod n = c
ciphertext = [pow(ch, e, n) for ch in plaintext_encryption]
ciphertext_alphabet = [chr((ch % 26) + 65) for ch in ciphertext]

print("Ciphertext: ", "".join(ciphertext_alphabet))

plaintext_decryption = [pow(ch, d, n) for ch in ciphertext]
decrypted_text = "".join(chr(ch) for ch in plaintext_decryption)
print("Plaintext after decryption: ", decrypted_text)