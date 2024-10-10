
def criba(n):
  
    primes = []  
    not_prime = set()  

    # Iterar desde 2 hasta n
    for i in range(2, n + 1):
        if i in not_prime:  # Si el número ya está en not_prime, no es primo
            continue

        # Agregar todos los múltiplos de i al conjunto not_prime
        for j in range(i * 2, n + 1, i):
            not_prime.add(j)
        primes.append(i)
    return primes

# Solicitar al usuario que ingrese un número entero positivo n
n = int(input("Ingrese un entero positivo n: "))

# Llamar a la función criba y almacenar el resultado en una lista de primos
primos = criba(n)

# Imprimir el resultado
print(f"Los primos menores o iguales a {n} son {primos}")
