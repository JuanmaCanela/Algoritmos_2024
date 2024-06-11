#Desarrollar una función recursiva que permita listar los elementos de vector/lista de manera inversa al que están cargados.
#Preferentemente la función solo debe tener un parámetro que es la lista de elementos.

def inversa(lista):
    if len(lista) == 0:
        return lista
    else:
        print(lista[-1])
        inversa(lista[:-1])

lista = [1, 2, 3, 4, 5]

inversa(lista)