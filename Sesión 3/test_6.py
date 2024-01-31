"""Uso del flujo condicional 'if'"""

var1 = int(input("Ingrese su primer dato numérico: "))
var2 = int(input("Ingrese su segundo dato numérico: "))

if var1 > var2:
    print("El valor de var1 es mayor que el segundo valor ingresado")
elif var1 == var2:
    print("Los valor ingresador son iguales")
else:
    print("El valor de var1 no es mayor que que la de var2")