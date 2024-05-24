#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”.
#Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

from pila import Stack

pila_episodio_v = Stack()
pila_episodio_v.push('Luke Skywalker')
pila_episodio_v.push('Darth Vader')
pila_episodio_v.push('Han Solo')
pila_episodio_v.push('Leia Organa')
pila_episodio_v.push('Yoda')

pila_episodio_vii = Stack()
pila_episodio_vii.push('Rey')
pila_episodio_vii.push('Finn')
pila_episodio_vii.push('Han Solo')
pila_episodio_vii.push('Leia Organa')
pila_episodio_vii.push('Luke Skywalker')
pila_episodio_vii.push('Kylo Ren')

def interseccion_pilas(pila1, pila2):
    interseccion = []
    pila_aux1 = Stack()
    pila_aux2 = Stack()

    personajes_pila1 = []
    while pila1.size() > 0:
        personaje = pila1.pop()
        personajes_pila1.append(personaje)
        pila_aux1.push(personaje)

    while pila_aux1.size() > 0:
        pila1.push(pila_aux1.pop())

    while pila2.size() > 0:
        personaje = pila2.pop()
        if personaje in personajes_pila1:
            interseccion.append(personaje)
        pila_aux2.push(personaje)

    while pila_aux2.size() > 0:
        pila2.push(pila_aux2.pop())

    return interseccion

interseccion = interseccion_pilas(pila_episodio_v, pila_episodio_vii)
print("Personajes que aparecen en ambos episodios:", interseccion)