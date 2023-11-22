import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


p = 1013
q = 1021

n = p * q
phi_n = (p - 1) * (q - 1)

e = 65537
d = 0


for candidate_d in range(1, phi_n):
    if (e * candidate_d) % phi_n == 1:
        d = candidate_d
        break

if d == 0:
    raise ValueError("Modular inverse does not exist")


def sign_file(filename, d, n):
    with open(filename, "rb") as f:
        message_bytes = f.read()
    message_int = int.from_bytes(message_bytes, byteorder="big")
    signature = pow(message_int, d, n)
    return signature


def verify_file(filename, signature, e, n):
    with open(filename, "rb") as f:
        message_bytes = f.read()
    message_int = int.from_bytes(message_bytes, byteorder="big")
    decrypted_signature = pow(signature, e, n)
    return message_int == decrypted_signature


filename = r"C:\Users\harsh\OneDrive - pdpu.ac.in\HARSH\_STUDY MATERIAL\SEM 5\Information Security\Information Security Lab\PRACTICE\InfoSec\RSA_encrypt.py"
signature = sign_file(filename, d, n)

# Verify the signature of the file using the sender's public key
is_valid = verify_file(filename, signature, e, n)

print("File:", filename)
print("Signature:", signature)
print("Is Sender Authentic?:", is_valid)
