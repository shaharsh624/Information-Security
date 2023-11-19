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
