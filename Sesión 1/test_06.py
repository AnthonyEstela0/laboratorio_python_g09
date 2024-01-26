
"""Conversión de datos"""

"""De string: str a enteros: int"""

var_1 ="700"
var_2 =35000
var_3 = 40.58

suma_1 = var_2 + var_3
print("El valor de suma_1 es: {}".format(suma_1))

#Esta suma no es posible por ser un valor string y otro entero
#suma_2 = var_1 + var_2
#print("El valor de suma_2 es: {}".format(suma_2))

suma_3 = int(var_1) + var_2
print("El valor de suma_3 es: {}".format(suma_3))

"""Suma de dos variables: int + float = """

suma_4 = var_2 + var_3
print("El valor de suma_4 es: {}".format(suma_4))

var_4 = int(suma_4)
print(var_4)


var_4 ="400"
var_5 =1200
var_6 = 3.14

suma_5 = var_4 + str(var_5) + str(var_6)
print("El valor de suma_5 es: {}".format(suma_5))
