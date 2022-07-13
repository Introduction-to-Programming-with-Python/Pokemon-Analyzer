import random

def cargar_pokemones() -> list:
    lista_pokemon = []
    # TODO: cargar archivo de pokemones
    archivo_pokemones = open('./Data/pokemon.csv')

    # TODO: leer el encabezado y guardarlo en una variable llamada atributos
    primera_linea = archivo_pokemones.readline()
    atributos = primera_linea.replace("\n", "").split(",")

    # TODO: crear los pokemones y meterlos en la lista
    
    linea = archivo_pokemones.readline()
    while len(linea) > 0:
        datos = linea.replace("\n", "").split(",")
        pokemon = {}
        for i, a in enumerate(atributos):
            pokemon[a] = datos[i]
        lista_pokemon.append(pokemon)
        linea = archivo_pokemones.readline()

    # TODO: cerrar el archivo
    archivo_pokemones.close()

    return lista_pokemon

#print(cargar_pokemones())

def buscar_pokemon(lista: list, id: str) -> dict:
    # TODO: Hacer un recorrido parcial sobre la lista

    buscado = None

    for i in lista:
        if i["id"] == id:
            buscado = i

    return buscado

#print(buscar_pokemon(cargar_pokemones(), "1"))


def cargar_estadisticas(lista_pokemon: list) -> list:

    nombres_estadisticas = {
        "1": "hp",
        "2": "attack",
        "3": "defense",
        "4": "special-attack",
        "5": "special-defense",
        "6": "speed",
        "7": "accuracy",
        "8": "evasion",
    }

    archivo_estadisticas=open('./Data/pokemon_estadisticas.csv')
    linea = archivo_estadisticas.readline()
    linea = archivo_estadisticas.readline()

    lista_pokemon_actualizada = []
    
    while len(linea) > 0:
        datos = linea.replace("\n", "").split(",")
        id_pokemon = datos[0]
        id_estadistica = datos[1]
        valor_estadistica = datos[2]
        nombre_estadistica = nombres_estadisticas[id_estadistica]
        pokemon = buscar_pokemon(lista_pokemon,id_pokemon)
        pokemon[nombre_estadistica] = valor_estadistica
        if pokemon not in lista_pokemon_actualizada:
            lista_pokemon_actualizada.append(pokemon)
        linea = archivo_estadisticas.readline()
        
    archivo_estadisticas.close()

    return lista_pokemon_actualizada

#print(cargar_estadisticas(cargar_pokemones()))


def capturar_10_pokemones(lista: list):
    # Acceder a 10 elementos aleatorios usando for in range(0,10)

    capturados = []
    pokemon = ""

    for i in range(0,10):
        diccionario_pokemon = lista[random.randint(0, len(lista)-1)]
        id_pokemon = diccionario_pokemon["id"]
        nombre_pokemon = diccionario_pokemon["identifier"]
        pokemon = id_pokemon + " " + nombre_pokemon
        capturados.append(pokemon)

    return capturados

#print(capturar_10_pokemones(cargar_pokemones()))


def dar_maximo_pokemon(lista_pokemon: list, caracteristica: str) -> dict:
    # TODO dada una característica, buscar en la lista el pokemon que tiene el mayor valor
    
    lista = lista_pokemon
    elegido = ""
    maximo = 0

    for i in lista:
        if int(i[caracteristica]) > maximo:
            maximo = int(i[caracteristica])
            elegido = i
        
    return elegido

#print(dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), "attack"))


def dar_minimo_pokemon(lista_pokemon: list, caracteristica: str) -> dict:
    # TODO dada una característica, buscar en la lista el pokemon que tiene el menor valor

    lista = lista_pokemon
    elegido = ""
    maximo = (dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), caracteristica))
    maximo = int(maximo[caracteristica])

    for i in lista:
        if int(i[caracteristica]) < maximo:
            maximo = int(i[caracteristica])
            elegido = i
        
    return elegido

#print(dar_minimo_pokemon(cargar_estadisticas(cargar_pokemones()), "special-attack"))


def hacer_equipo_balanceado(lista_pokemon: list) -> str:
    # TODO Crear un equipo llamando a los métodos creados anteriormente, # cumpliendo los requerimientos del enunciado
    
    datos = {"mas_ataque": dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), "attack"), 
    "mas_defensa": dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), "special-defense"), 
    "mas_debil": dar_minimo_pokemon(cargar_estadisticas(cargar_pokemones()), "hp"),
    "mas_lento": dar_minimo_pokemon(cargar_estadisticas(cargar_pokemones()), "speed"),
    "mas_alto": dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), "height"),
    "mas_pequeño": dar_minimo_pokemon(cargar_estadisticas(cargar_pokemones()), "height"),
    "mas_pesado":dar_maximo_pokemon(cargar_estadisticas(cargar_pokemones()), "weight"),}

    fila = "{0} \t {1} \t {2} \t {3} \t {4} \t {5} \t {6} \t {7}"

    caracteristicas = {"0": "identifier", "1": "hp", "2": "attack", "3": "defense", "4":"special-defense", "5": "speed", "6": "height", "7": "weight"}
    atributos = ["mas_ataque", "mas_defensa", "mas_debil", "mas_lento", "mas_alto", "mas_pequeño", "mas_pesado"]

    #print("Nombre\t HP\tAtaque\tDefensa\tDefensa-esp\tVelocidad\tAltura\tPeso")

    caracteristica = ""
    for i in range(0,7):
        caracteristica = caracteristicas[str(i)]
        mas = atributos[i]
        pokemon = datos[mas]
        nombre = pokemon["identifier"]
        hp = pokemon["hp"]
        ataque = pokemon["attack"]
        defensa = pokemon["defense"]
        defensaesp = pokemon["special-defense"]
        velocidad = pokemon["speed"]
        altura = pokemon["height"]
        peso = pokemon["weight"]

        formateo = fila.format(nombre, hp, ataque, defensa, defensaesp, velocidad, altura, peso)

        print(formateo)

        fila = "{0}\t {1}\t {2}\t {3}\t {4}\t {5}\t {6}\t {7}"

    return ""

print(hacer_equipo_balanceado(cargar_estadisticas(cargar_pokemones())))