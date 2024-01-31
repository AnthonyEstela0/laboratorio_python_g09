"""Usando las propiedades de cadenas a strings"""

"""
Requisitos:

- Ingresar tu nombre y apellido por consola (cada valor tiene que estar en una variable distinta)
- Concatenar ambos valores en una sola variable
- Obtener el tamaño de tu nombre completo
- Imprimir resultado final todo en mayusculas
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al del apellido
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

identificacion = nombre + " " + apellido

print("El tamaño de tu nombre completo es: {}".format(len(identificacion)))
print("Mi nombre es nombre completo es: {}".format(identificacion.upper()))

if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor al del apellido")
else:
    print("El tamaño del nombre no es mayor al del apellido")

