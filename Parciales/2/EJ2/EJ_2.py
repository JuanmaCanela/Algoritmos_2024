from grafo import Graph

# a) Cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan
grafo_star_wars = Graph(dirigido=False)

# d) Cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", 
    "C-3PO", "Leia", "Rey", "Kylo Ren", 
    "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

for personaje in personajes:
    grafo_star_wars.insert_vertice(personaje)

relaciones = [
    ("Luke Skywalker", "Darth Vader", 3),
    ("Luke Skywalker", "Yoda", 2),
    ("Luke Skywalker", "Leia", 1),
    ("Darth Vader", "Yoda", 1),
    ("Leia", "Han Solo", 3),
    ("Han Solo", "Chewbacca", 5),
    ("Chewbacca", "C-3PO", 2),
    ("Rey", "Kylo Ren", 3),
    ("Luke Skywalker", "R2-D2", 2),
    ("Leia", "R2-D2", 1),
    ("BB-8", "R2-D2", 2),
    ("Leia", "C-3PO", 4),
    ("Leia", "Yoda", 1)
]

for origen, destino, peso in relaciones:
    grafo_star_wars.insert_arista(origen, destino, peso)

# b) Hallar el árbol de expansión minino y determinar si contiene a Yoda
arbol_minimo = grafo_star_wars.kruskal("Luke Skywalker")

# Verificamos si está Yoda
contiene_yoda = any("Yoda" in arbol for arbol in arbol_minimo)
print("El árbol de expansión mínimo contiene a Yoda:", contiene_yoda)

# c) Determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son
max_episodios = 0
personajes_max_episodios = ("", "")

# Buscamos la arista con el mayor número de episodios compartidos
for nodo in grafo_star_wars.elements:
    for arista in nodo['aristas']:
        if arista['peso'] > max_episodios:
            max_episodios = arista['peso']
            personajes_max_episodios = (nodo['value'], arista['value'])

print(f"El número máximo de episodios compartidos es {max_episodios}, entre {personajes_max_episodios[0]} y {personajes_max_episodios[1]}")
