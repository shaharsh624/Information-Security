def get_key_matrix(plaintext):
    cols = len(plaintext) // 2
    P = [[0] * cols for _ in range(2)]
    length = 0
    while length != len(plaintext):
        for i in range(2):
            for j in range(cols):
                P[i][j] = ord(plaintext[length]) - 65
                length += 1
    return P


def get_plain_text_matrix(key):
    K = [[0] * (len(key) // 2) for _ in range(2)]
    length = 0
    for i in range(len(key) // 2):
        for j in range(2):
            K[j][i] = ord(key[length]) - 65
            length += 1
    return K


def mat_mul(matrix1, r1, c1, matrix2, r2, c2):
    ans = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            ans[i][j] = 0
            for k in range(c1):
                ans[i][j] += matrix1[i][k] * matrix2[k][j]
    return ans


def encrypt(plaintext, key):
    P = get_plain_text_matrix(plaintext)
    K = get_key_matrix(key)
    Encrypted = mat_mul(K, 2, len(key) // 2, P, 2, len(plaintext) // 2)

    encrypted = ""
    for i in range(len(plaintext) // 2):
        for j in range(2):
            encrypted += chr(Encrypted[j][i] % 26 + 65)

    return encrypted


def decrypt(ciphertext, key):
    C = get_plain_text_matrix(ciphertext)
    K = get_key_matrix(key)
    K_inv = [[K[1][1], -K[0][1]], [-K[1][0], K[0][0]]]
    det = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    det_inv = pow(det, -1, 26)
    for i in range(2):
        for j in range(len(key) // 2):
            K_inv[i][j] = (K_inv[i][j] * det_inv) % 26
    Decrypted = mat_mul(K_inv, 2, len(key) // 2, C, 2, len(ciphertext) // 2)

    decrypted = ""
    for i in range(len(ciphertext) // 2):
        for j in range(2):
            decrypted += chr(Decrypted[j][i] % 26 + 65)

    return decrypted


plaintext = "EXAM"
key = "HILL"
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, key)
print("Decrypted plaintext:", decrypted_plaintext)
