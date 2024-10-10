def Algoritmo_euclides(a, b):

    while a % b != 0:
        r = a % b
        a = b
        b = r
        
    return b


a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))


RAlgoritmo = Algoritmo_euclides(a, b)

print(f"El mcd de {a} y {b} es {RAlgoritmo}")