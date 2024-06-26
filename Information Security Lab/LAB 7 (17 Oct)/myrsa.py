import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(min, max):
    prime = random.randint(min, max)
    if not is_prime(prime):
        while not is_prime(prime):
            prime = random.randint(min, max)
    return prime


def mod_inverse(e, phi_of_n):
    for d in range(3, phi_of_n):
        if ((d * e) % phi_of_n) == 1:
            return d
    raise ValueError("Mod Inverse doesn't exist!")


def RSA(p, q):
    n = p * q
    phi_of_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_of_n - 1)
    while gcd(e, phi_of_n) != 1:
        e = random.randint(3, phi_of_n - 1)

    d = mod_inverse(e, phi_of_n)

    return n, e, d


if __name__ == "__main__":
    p, q = generate_prime(100, 500), generate_prime(100, 500)

    while p == q:
        q = generate_prime(100, 500)

    n, e, d = RSA(p, q)

    print(f"\nPublic Key: ({e}, {n})")
    print(f"Private Key: ({d}, {n})")

    #  Encryption
    message = "Hello World"
    plain_num = [ord(ch) for ch in message]

    cipher_num = [(M**e) % n for M in plain_num]
    cipher_text = "".join([chr((n % 26) + 65) for n in cipher_num])

    # Decryption
    plain_num = [(C**d) % n for C in cipher_num]
    plain_text = "".join([chr(n) for n in plain_num])

    print(f"\nOriginal Message: {message}")
    print(f"Encrypted Text: {cipher_text}")
    print(f"Decrypted Text: {plain_text}")
