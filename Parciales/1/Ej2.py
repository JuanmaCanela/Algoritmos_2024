#Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

from pila import Stack
from dino import dinosaurios

pila_dinosaurios = Stack()
for dino in dinosaurios:
    pila_dinosaurios.push(dino)

#a) Contar cuantas especies hay
def contar_especies(pila):
    especies = set()
    pila_aux = Stack()

    while pila.size() > 0:
        dinosaurio = pila.pop()
        especies.add(dinosaurio['especie'])
        pila_aux.push(dinosaurio)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return len(especies)

#b) Determinar cuantos descubridores distintos hay
def contar_descubridores(pila):
    descubridores = set()
    pila_aux = Stack()

    while pila.size() > 0:
        dinosaurio = pila.pop()
        descubridores.add(dinosaurio['descubridor'])
        pila_aux.push(dinosaurio)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return len(descubridores)

#c) Mostrar todos los dinosaurios que empiecen con T
def dinosaurios_con_T(pila):
    dinosaurios_T = []
    pila_aux = Stack()

    while pila.size() > 0:
        dinosaurio = pila.pop()
        if dinosaurio['nombre'].startswith('T'):
            dinosaurios_T.append(dinosaurio)
        pila_aux.push(dinosaurio)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return dinosaurios_T

#d) Mostrar todos los dinosaurios que pesen menos de 275 Kg
def dinosaurios_275(pila):
    dinosaurios_menos_275 = []
    pila_aux = Stack()

    while pila.size() > 0:
        dinosaurio = pila.pop()
        peso = int(dinosaurio['peso'].split()[0])
        if peso < 275:
            dinosaurios_menos_275.append(dinosaurio)
        pila_aux.push(dinosaurio)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return dinosaurios_menos_275

#e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S
def pila_con_AQS(pila):
    pila_AQS = Stack()
    pila_aux = Stack()

    while pila.size() > 0:
        dinosaurio = pila.pop()
        if dinosaurio['nombre'][0] in ['A', 'Q', 'S']:
            pila_AQS.push(dinosaurio)
        pila_aux.push(dinosaurio)

    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return pila_AQS


print("Cantidad de especies:", contar_especies(pila_dinosaurios))
print()
print("Cantidad de descubridores distintos:", contar_descubridores(pila_dinosaurios))
print()
print("Dinosaurios que empiezan con T:", dinosaurios_con_T(pila_dinosaurios))
print()
print("Dinosaurios que pesan menos de 275 Kg:", dinosaurios_275(pila_dinosaurios))
print()
pila_dinosaurios_AQS = pila_con_AQS(pila_dinosaurios)
print("Dinosaurios que comienzan con A, Q, S:", [d['nombre'] for d in pila_dinosaurios_AQS._Stack__elements])