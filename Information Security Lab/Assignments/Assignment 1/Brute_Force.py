# Method 1
password = input("Enter password to guess (alphabets of length 4): ")
alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', "Z",
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', "z",
]
for a in alphabets:
    for b in alphabets:
        for c in alphabets:
            for d in alphabets:
                guess = a + b + c + d
                if password == guess:
                    print(guess)
                    break


# Method 2 (Optimized)
password = input("Enter the password: ")
guess = ""
count = 0
for i in range(len(password)):
    character = password[i]
    for a in range(256):
        if character == chr(a):
            guess += character
            break
print(guess)
