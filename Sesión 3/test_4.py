"""
Requisitos:
- Dentro de una empresa se va a solicitar pedir nombre y apellido de empleado.
- Distrito de residencia
- Sueldo y calculo del bono final del año, que será el triple de su sueldo mensual menos el 10 porciento
- Todos estos datos van a ingresar a una lista
- Por asignación múltiple de variables asignar los valores de esta lista a 3 nuevas variables
- Mostrar en la terminal el mensaje de "'Nombre' 'apellido' recibirá 'bono' soles"
"""

nombre_apellido = input("Ingrese su nombre y apellido: ")
distrito = input("Ingrese su Distrito de residencia: ")
sueldo = input("Ingrese su sueldo: ")

bonofinal = 0.9*3*int(sueldo)

lista = [nombre_apellido, distrito, sueldo, bonofinal]

identidad, localidad, remuneración, compensacion = lista

print("{} recibirá {} soles".format(identidad, compensacion))

