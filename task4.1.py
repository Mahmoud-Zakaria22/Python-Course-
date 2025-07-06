def is_prime(n):
    if n == 2 or n==3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n % 2 != 0 and n % 3 != 0:
        return True
print(is_prime(14))
