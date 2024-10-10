import numpy as np

def criba(n):
    primes = []
    not_prime = set()

    for i in range(2, n + 1):
        if i in not_prime:
            continue

        for j in range(i * 2, n + 1, i):
            not_prime.add(j)

        primes.append(i)

    return primes

def isprime(n):
    if n < 2:
        return f"El número {n} no es primo, ya que es menor que 2."

    prime_list = criba(int(np.sqrt(n)) + 1)

    for prime in prime_list:
        if n % prime == 0:
            return f"El número {n} no es primo, pues lo divide {prime}."

    return f"El número {n} es primo."

try:
    n = int(input("Ingrese un entero positivo n: "))
    print(isprime(n))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
