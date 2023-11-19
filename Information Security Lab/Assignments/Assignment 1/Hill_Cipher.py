def main():
    cont = 1
    while cont != 0:
        print("Enter 1 for encryption, 2 for decryption: ")
        choice = int(input())

        if choice == 1:
            print("Enter key of length 4: ")
            key = input()
            print("Enter plain text of length 4: ")
            plain = input()

            k = [[0] * 2 for _ in range(2)]
            count = 0
            for i in range(2):
                for j in range(2):
                    k[i][j] = ord(key[count]) % 97
                    count += 1

            p = [[0] for _ in range(2)]
            q = [[0] for _ in range(2)]
            count = 0
            for i in range(2):
                for j in range(1):
                    p[i][j] = ord(plain[count]) % 97
                    count += 1
            for i in range(2):
                for j in range(1):
                    q[i][j] = ord(plain[count]) % 97
                    count += 1

            d1 = [[0] for _ in range(2)]
            for i in range(2):
                for j in range(1):
                    d1[i][j] = (k[i][0] * p[0][j] + k[i][1] * p[1][j]) % 26

            d2 = [[0] for _ in range(2)]
            for i in range(2):
                for j in range(1):
                    d2[i][j] = (k[i][0] * q[0][j] + k[i][1] * q[1][j]) % 26

            for i in range(2):
                for j in range(1):
                    print(chr(d1[i][j] + 97), end="")
            for i in range(2):
                for j in range(1):
                    print(chr(d2[i][j] + 97), end="")
            print()

            print("Enter 1 to continue and 0 to exit: ")
            cont = int(input())

        elif choice == 2:
            print("Enter key of length 4: ")
            key = input()
            print("Enter cipher text of length 4: ")
            cipher = input()

            k = [[0] * 2 for _ in range(2)]
            count = 0
            for i in range(2):
                for j in range(2):
                    k[i][j] = ord(key[count]) % 97
                    count += 1

            p = [[0] for _ in range(2)]
            q = [[0] for _ in range(2)]
            count = 0
            for i in range(2):
                for j in range(1):
                    p[i][j] = ord(cipher[count]) % 97
                    count += 1
            for i in range(2):
                for j in range(1):
                    q[i][j] = ord(cipher[count]) % 97
                    count += 1

            det = k[0][0] * k[1][1] - k[1][0] * k[0][1]
            if det < 0:
                det = 26 + det
            temp = k[0][0]
            k[0][0] = k[1][1]
            k[1][1] = temp
            k[0][1] = - k[0][1] + 26
            k[1][0] = - k[1][0] + 26

            inverse = 1
            while (det * inverse) % 26 != 1:
                inverse += 1
            det = inverse

            for i in range(2):
                for j in range(2):
                    k[i][j] = (k[i][j] * det) % 26

            d1 = [[0] for _ in range(2)]
            for i in range(2):
                for j in range(1):
                    d1[i][j] = (k[i][0] * p[0][j] + k[i][1] * p[1][j]) % 26

            d2 = [[0] for _ in range(2)]
            for i in range(2):
                for j in range(1):
                    d2[i][j] = (k[i][0] * q[0][j] + k[i][1] * q[1][j]) % 26

            for i in range(2):
                for j in range(1):
                    print(chr(d1[i][j] + 97), end="")
            for i in range(2):
                for j in range(1):
                    print(chr(d2[i][j] + 97), end="")
            print()

            print("Enter 1 to continue and 0 to exit: ")
            cont = int(input())

        else:
            print("Enter number 0 or 1")
            print("Enter 1 to continue and 0 to exit: ")
            cont = int(input())


if __name__ == "__main__":
    main()
