"""Diccionarios en Python"""

"""del = eliminar"""

var_1 = {"nombre": "Margarita","edad": 27, "promedio": 15}

print("Nuestro primer diccionario tiene el siguiente contenido: {}".format(var_1))

"""Quitamos elementos en un nuevo key a mi diccionario"""

del var_1["nombre"]
del var_1["edad"]

print("Mi diccionario actualizado tiene los siguientes valores:{}".format(var_1))