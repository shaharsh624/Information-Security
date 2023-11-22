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

rails = 10
ciphertext = "Keenswoh osud todhtgg o!trr!l r or nicinoiugAek  wult  c egonh emiihoddoohafnte !Kftgit s  no"

plaintext = decrypt(ciphertext, rails)
print("Decrypted Text:", plaintext)
