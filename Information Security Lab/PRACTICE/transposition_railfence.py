def encrypt(plaintext, rails):
    fence = [""] * rails

    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail] = fence[rail] + char
        rail = rail + direction

        if rail == 0 or rail == rails - 1:
            direction = -direction

    ciphertext = ""
    for text in fence:
        ciphertext = ciphertext + text

    return ciphertext


def decrypt(ciphertext, rails):
    fence = []
    for _ in range(rails):
        rail = [''] * len(ciphertext)
        fence.append(rail)

    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        fence[rail][i] = 'x'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction = -direction

    index = 0
    for row in range(rails):
        for col in range(len(ciphertext)):
            if fence[row][col] == 'x':
                fence[row][col] = ciphertext[index]
                index += 1

    plaintext = ''
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        if fence[rail][i] != 'x':
            plaintext += fence[rail][i]

        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    return plaintext


rails = 2
plaintext = "MEETMEATTHEPARK"

ciphertext = encrypt(plaintext, rails)
print("Encrypted Text - ", ciphertext)

plaintext = decrypt(ciphertext, rails)
print("Decrypted Text:", plaintext)