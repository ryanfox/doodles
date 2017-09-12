import sympy


def digits(num):
    return len(str(num))


def print_primes(num_digits):
    if sympy.isprime(num_digits):
        for prime in sympy.primerange(10 ** (num_digits - 1), 10 ** num_digits):
            print(prime)


# handle the only even prime
print_primes(2)

i = 3
while True:
    print_primes(i)
    i += 2
