from arbol_avl import BinaryTree

pokemons = [
    {"name": "Bulbasaur", "number": 1, "type": ["Planta", "Veneno"]},
    {"name": "Ivysaur", "number": 2, "type": ["Planta", "Veneno"]},
    {"name": "Charmander", "number": 4, "type": ["Fuego"]},
    {"name": "Charmeleon", "number": 5, "type": ["Fuego"]},
    {"name": "Squirtle", "number": 7, "type": ["Agua"]},
    {"name": "Jolteon", "number": 135, "type": ["Eléctrico"]},
    {"name": "Lycanroc", "number": 745, "type": ["Roca"]},
    {"name": "Tyrantrum", "number": 697, "type": ["Roca", "Dragón"]}
]

nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

# a) Insertar datos en los árboles
for pokemon in pokemons:

    nombre_tree.insert_node(pokemon["name"], pokemon)
    
    numero_tree.insert_node(pokemon["number"], pokemon)
    
    for tipo in pokemon["type"]:
        tipo_tree.insert_node(tipo, pokemon)

# b) Mostrar todos los datos de un Pokémon por número y búsqueda aproximada por nombre
print()
print('b) Mostrar todos los datos de un Pokémon por número y búsqueda aproximada por nombre')
def buscar_por_numero_y_nombre(numero, nombre_inicial):
    print("\nBúsqueda por número:")
    resultado_numero = numero_tree.search(numero)
    if resultado_numero:
        print(f"Número {numero}: {resultado_numero.other_value}")
    else:
        print(f"Pokémon con número {numero} no encontrado.")

    print("\nBúsqueda por nombre (proximidad):")
    print(f"Pokémons que coinciden con '{nombre_inicial}':")
    nombre_tree.proximity_search(nombre_inicial)

buscar_por_numero_y_nombre(135, "Bul")

# c) Mostrar los nombres de todos los Pokémon de tipos Agua, Fuego, Planta y Eléctrico
print()
print('c) Mostrar los nombres de todos los Pokémon de tipos Agua, Fuego, Planta y Eléctrico')
def mostrar_por_tipo(tipos):
    for tipo in tipos:
        print(f"\nPokémons de tipo {tipo}:")

        def buscar_pokemons_por_tipo(root, tipo):
            if root is not None:
                buscar_pokemons_por_tipo(root.left, tipo)
                if root.value == tipo:
                    print(root.other_value["name"])
                buscar_pokemons_por_tipo(root.right, tipo)

        buscar_pokemons_por_tipo(tipo_tree.root, tipo)

mostrar_por_tipo(["Agua", "Fuego", "Planta", "Eléctrico"])

# d) Listado en orden ascendente por número y nombre
print()
print('d) Listado en orden ascendente por número y nombre')
print("\nListado en orden ascendente por número:")
numero_tree.inorden()

print("\nListado en orden ascendente por nombre:")
nombre_tree.inorden()

# e) Mostrar todos los datos de Jolteon, Lycanroc y Tyrantrum
print()
print('e) Mostrar todos los datos de Jolteon, Lycanroc y Tyrantrum')
def mostrar_datos_pokemons(nombres):
    for nombre in nombres:
        resultado = nombre_tree.search(nombre)
        if resultado:
            print(f"\nDatos de {nombre}: {resultado.other_value}")
        else:
            print(f"\n{nombre} no encontrado en el árbol de nombres.")

mostrar_datos_pokemons(["Jolteon", "Lycanroc", "Tyrantrum"])

# f) Determinar cuántos Pokémon hay de tipo Eléctrico y Acero
print()
print('f) Determinar cuántos Pokémon hay de tipo Eléctrico y Acero')
def contar_pokemons_por_tipo(tipos):
    contador = {tipo: 0 for tipo in tipos}
    
    for tipo in tipos:
        def contar_tipo(root):
            if root is not None:
                if root.value == tipo:
                    contador[tipo] += 1
                contar_tipo(root.left)
                contar_tipo(root.right)
                
        contar_tipo(tipo_tree.root)

    for tipo, count in contador.items():
        print(f"\nCantidad de Pokémons de tipo {tipo}: {count}")

contar_pokemons_por_tipo(["Eléctrico", "Acero"])