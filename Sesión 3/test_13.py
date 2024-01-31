"""Usando las propiedades de cadenas a strings"""

"""Concatenación"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_completo = "El nombre completo es: " + nombre + " " + apellido
print(nombre_completo)

nombre_completo2 = "El nombre completo es: {} {}".format(nombre, apellido)
print(nombre_completo2)