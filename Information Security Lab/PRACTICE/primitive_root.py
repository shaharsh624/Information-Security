def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def phi(n):
    group = set()
    for i in range(1, n):
        if gcd(i, n) == 1:
            group.add(i)

    return len(group)


def is_primitive_root(a, n):
    residues = set()
    for i in range(1, n):
        residue = pow(a, i, n)
        if residue in residues:
            return False
        residues.add(residue)
    return len(residues) == phi(n)


def find_primitive_roots(n):
    primitive_roots = []
    for a in range(2, n):
        if is_primitive_root(a, n):
            primitive_roots.append(a)
    return primitive_roots


n = int(input("Enter a number: "))
primitive_roots = find_primitive_roots(n)

print(f"The primitive roots of {n} are: {primitive_roots}")
