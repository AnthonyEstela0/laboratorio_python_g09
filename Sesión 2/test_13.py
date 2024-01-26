"""Listas en Python"""

"""Listas (del): Elimina un valor indicando el indice del valor de la lista"""

paises = []

paises.append("Perú")
paises.append("Brasil")
paises.append("Canada")
paises.append("España")
paises.append("Chile")

print("Los valores de mi lista de paises son: {}".format(paises))

del paises[2]

print("Mi lista actualizada tiene los siguientes valores: {}".format(paises))