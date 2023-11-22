def ceaser_decryption(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            uppercase = char.isupper()
            if uppercase:
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            else:
                alphabet = "abcdefghijklmnopqrstuvwxyz"

            P = (alphabet.index(char) - key) % 26
            decrypted_text += alphabet[P]
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "Cb hvs qfwqysh twszr, dzomsfg poh, pckz, obr twszr, qfsohwbu ob slqwhwbu aohqv twzzsr kwhv oqhwcb obr ghfohsum.\nHvs qfckr qvssfg og hvs pozz wg vwh, obr hvs dzomsfg qvogs wh kwhv sbhvigwoga.\nQfwqysh pfwbug hcushvsf tfwsbrg obr tobg tcf tib obr hvfwzzwbu uoasg, qfsohwbu zoghwbu asacfwsg obr gvofsr acasbhg ct xcm."
key = 14

print(ceaser_decryption(ciphertext, key))
