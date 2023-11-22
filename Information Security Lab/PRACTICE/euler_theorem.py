def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient_function(m):
    count = 0
    for i in range(1, m):
        if gcd(i, m) == 1:
            count += 1
    return count

def power_modulo(a, b, m):
    result = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m

    return result

def eulers_theorem(a, m):
    if gcd(a, m) != 1:
        return "a and m must be coprime"

    phi_m = euler_totient_function(m)
    result = power_modulo(a, phi_m, m)
    return f"{a}^{phi_m} ≡ {result} (mod {m})"

# Example usage
a = 1
m = 1000
print(eulers_theorem(a, m))
