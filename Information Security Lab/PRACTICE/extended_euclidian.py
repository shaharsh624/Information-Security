def extended_euclid(a, b):
    if a < b:
        a, b = b, a
    mod_inverse = extended_euclid_rec(a, b, 0, 1)
    if mod_inverse < 0:
        mod_inverse += a
    return mod_inverse


def extended_euclid_rec(a, b, t1, t2):
    if b == 0:
        return t1
    q = a // b
    r = a % b
    t = t1 - t2 * q
    print(q, a, b, r, t1, t2, t)

    return extended_euclid_rec(b, r, t2, t)


if __name__ == "__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    mod = extended_euclid(a, b)
    print(f"{a} mod {b} = {mod}")
