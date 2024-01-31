"""Uso del flujo condicional 'if'"""
"""if ternario"""

"""
Requisitos:
    - Ingresar por teclado el sueldo de un empleado
    - Si el sueldo es mayor a 3000 imprimir "Su sueldo no tiene bonificación"
    - Caso contrario: "Su sueldo tiene bonifiación este año"
"""

sueldo = int(input("Ingrese su sueldo"))

final = "Su sueldo no tiene bonificación" if sueldo > 3000 else "Su sueldo tiene bonifiación este año"
print(final)