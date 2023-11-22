def euclid(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return euclid(b, a % b)


if __name__ == "__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    gcd = euclid(a, b)
    print(f"gcd({a},{b}) = {gcd}")
