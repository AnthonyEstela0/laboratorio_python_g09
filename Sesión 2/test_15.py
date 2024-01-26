
lista_1 = []
lista_2 = []

lista_1.append("Anthony Estela")
lista_1.append(28)
lista_1.append("Ing. Telecomunicaciones")

lista_1.append("Humberto Chavez")
lista_1.append(25)
lista_1.append("Ing. de Sistemas")

suma_1 = lista_1 + lista_2

print("La suma de mi lista_1 + lista_2 es: {}".format(suma_1))

suma_1.reverse()

print("El inverso de la suma_1 es: {}".format(suma_1))

del suma_1[1]
del suma_1[3]

print("mi nueva lista es: {}".format(suma_1))





