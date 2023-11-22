def ceaser_encryption(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            uppercase = char.isupper()
            if uppercase:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            else:
                alphabet = "abcdefghijklmnopqrstuvwxyz"

            C = (alphabet.index(char) + key) % 26
            encrypted_text += alphabet[C]
        else:
            encrypted_text += char
    return encrypted_text

plaintext = "On the cricket field, players bat, bowl, and field, creating an exciting match filled with action and strategy.\nThe crowd cheers as the ball is hit, and the players chase it with enthusiasm.\nCricket brings together friends and fans for fun and thrilling games, creating lasting memories and shared moments of joy."
key = 14

print(ceaser_encryption(plaintext, key))
