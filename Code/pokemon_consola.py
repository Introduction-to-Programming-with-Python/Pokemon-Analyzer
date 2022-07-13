import pokemon_funciones as poke

lista_pokemon = poke.cargar_pokemones()
poke.cargar_estadisticas(lista_pokemon)

print("Nombres de los primeros 20 pokemon:")
nombres = []
for p in lista_pokemon[0:20]:
    nombres.append(p["identifier"])
print(", ".join(nombres))

print("")

capturados = poke.capturar_10_pokemones(lista_pokemon)
print("Pokemon capturados:")
for c in capturados:
    print(c.split(" ")[1])

print("")

print("Equipo Balanceado:")
print(poke.hacer_equipo_balanceado(lista_pokemon))
