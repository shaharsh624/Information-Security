def encrypt(plaintext, rails):
    fence = [''] * rails

    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail] = fence[rail] + char
        rail = rail + direction

        if rail == 0 or rail == rails-1:
            direction = -direction

    ciphertext = ''
    for text in fence:
        ciphertext = ciphertext + text

    return ciphertext


rails = 10
plaintext = "Kohli goes down the ground! Kohli goes out of the ground! A magnificent strik into the crowd!"

ciphertext = encrypt(plaintext, rails)
print("Encrypted Text - ", ciphertext)
