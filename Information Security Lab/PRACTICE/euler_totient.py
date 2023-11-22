def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def euler_totient(n):
    group = set()
    for i in range(1, n):
        if gcd(i, n) == 1:
            group.add(i)

    return group


n = int(input("Enter a number: "))
group = euler_totient(n)
print(group)
print("phi(n) =", len(group))
