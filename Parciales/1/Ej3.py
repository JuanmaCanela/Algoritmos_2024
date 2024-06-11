#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie.
#Implementar las funciones necesarias para resolver las actividades enumeradas a continuación:
from Jedi import jedis

#a) Listado ordenado por nombre y por especie
def by_nom_esp(item):
    return item['name']+item['species']

print(jedis.sort(key=by_nom_esp))

#b) Mostrar toda la información de Ahsoka Tano y Kit Fisto
def info_jedi(nombre):
    for jedi in jedis:
        if jedi["name"] == nombre:
            return jedi
    return None

#c) Mostrar todos los padawan de Yoda y Luke Skywalker
def listar_padawans(maestros):
    padawans = []
    for jedi in jedis:
        if jedi["master"] in maestros:
            padawans.append(jedi["name"])
    return padawans

#d) Mostrar los Jedi de especie humana y twi'lek
def listar_humanos_twi_leks():
    return [jedi for jedi in jedis if jedi["species"] in ["Human", "Twi'lek"]]

#e) Listar todos los Jedi que comienzan con A
def listar_jedi_con_a():
    return [jedi for jedi in jedis if jedi["name"].startswith("A")]

#f) Mostrar los Jedi que usaron sable de luz de más de un color
def listar_jedi_mas_de_un_color():
    return [jedi for jedi in jedis if jedi["lightsaber_color"] and "/" in jedi["lightsaber_color"]]

#g) Indicar los Jedi que utilizaron sable de luz amarillo o violeta
def listar_jedi_amarillo_violeta():
    return [jedi for jedi in jedis if jedi["lightsaber_color"] and ("Yellow" in jedi["lightsaber_color"] or "Purple" in jedi["lightsaber_color"])]

#h) Indicar los nombres de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron
def listar_padawans_qg_mw():
    maestros = ["Qui-Gon Jinn", "Mace Windu"]
    padawans = []
    for jedi in jedis:
        if jedi["master"] in maestros:
            padawans.append(jedi["name"])
    return padawans

# i) Mostrar todos los Jedi que tengan el ranking de Grand Master
def listar_grand_masters():
    return [jedi for jedi in jedis if jedi["rank"] == "Grand Master"]

print("b) Información de Ahsoka Tano:")
print(info_jedi("Ahsoka Tano"))
print("b) Información de Kit Fisto:")
print(info_jedi("Kit Fisto"))

print("c) Padawans de Yoda y Luke Skywalker:")
print(listar_padawans(["Yoda", "Luke Skywalker"]))

print("d) Jedi de especie humana y twi'lek:")
print(listar_humanos_twi_leks())

print("e) Jedi que comienzan con A:")
print(listar_jedi_con_a())

print("f) Jedi que usaron sable de luz de más de un color:")
print(listar_jedi_mas_de_un_color())

print("g) Jedi que utilizaron sable de luz amarillo o violeta:")
print(listar_jedi_amarillo_violeta())

print("h) Padawans de Qui-Gon Jinn y Mace Windu:")
print(listar_padawans_qg_mw())

print("i) Jedi con el rango de Grand Master:")
print(listar_grand_masters())