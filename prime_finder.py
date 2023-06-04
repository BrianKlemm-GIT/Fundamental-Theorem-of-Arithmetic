import math


def sieve_of_eratosthenes(n):
    """Return a list of all primes less than or equal to n."""
    primes = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    primes_only = [p for p in range(2, n) if primes[p]]
    return primes_only


def needed_primes(n, existing_primes):
    all_primes = sieve_of_eratosthenes(n)
    new_primes = [p for p in all_primes if p not in existing_primes]
    return new_primes


def prime_finder(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
