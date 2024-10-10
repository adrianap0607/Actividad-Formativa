def Coeficientes_bezout(a, b):

    x0 = 1
    x1 = 0
    y0 = 0 
    y1 = 1

    while b != 0:
        q = a // b 
        a, b = b, a % b 
        x0, x1 = x1, x0 - q * x1 
        y0, y1 = y1, y0 - q * y1 

    return x0, y0


a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))

x, y = Coeficientes_bezout(a, b)
print(f"Los coeficientes de Bézout de {a} y {b} son {x} y {y}, respectivamente.")
