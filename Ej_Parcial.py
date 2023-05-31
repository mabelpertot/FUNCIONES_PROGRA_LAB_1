import json
import csv
from pprint import pprint
from copy import deepcopy
import re

'''FUNCIONA'''#0 Cargar los datos de los jugadores desde el archivo JSON
def parse_json_jugadores(nombre_archivo:str) -> list:
    archivo = open(nombre_archivo, "r")
    lista_json = json.load(archivo)["jugadores"]
    archivo.close()
    return deepcopy(lista_json)

"""Parsea un archivo JSON y devuelve una lista de jugadores.
    :param nombre_archivo: Nombre del archivo JSON a parsear.
    :return: Lista de jugadores en formato JSON.
    """

'''FUNCIONA'''#pregunta continuar
def pregunta_continuar() -> bool:
    preg_continuar = input("Quiere ver las estadísticas de otro jugador? S/N ")

    if preg_continuar.upper() == 'S':
        continuar = True
    else:
        continuar = False

    return continuar

'''FUNCIONA'''
# 1 Función para mostrar la lista de jugadores del Dream Team
def mostrar_lista_jugadores(lista: list) -> None:
    print("Lista de jugadores del Dream Team:")
    # Recorrer la lista de jugadores y mostrar sus nombres y posiciones
    for jugador in lista:
        print(f"{jugador['nombre']} - {jugador['posicion']}")
    """La función muestra por pantalla la lista de jugadores y sus posiciones, pero no devuelve ningún valor."""

'''FUNCIONA'''#2 Función para ordenar una lista de jugadores por posiciones.
def mostrar_estadisticas_jugador(lista) -> None:
    # Mostrar lista de jugadores con sus índices
    print("Lista de jugadores:")
    for i, jugador in enumerate(lista):
        print(f"{i+1}. {jugador['nombre']}")
#se recorrerá la lista de jugadores utilizando la función enumerate(), lo que permite obtener tanto el índice como el jugador en cada iteración. 
#se muestra por pantalla el índice incrementado en 1 y el nombre del jugador

    # Solicitar al usuario seleccionar un jugador por su índice
    seleccionado = input("Seleccione un jugador por su índice: ")
#La función isdigit() es un método de las cadenas de caracteres que devuelve True si todos los caracteres de la cadena son dígitos y False en caso contrario
    if seleccionado.isdigit():
        indice = int(seleccionado) - 1
        if 0 <= indice < len(lista):
            jugador = lista[indice]
            estadisticas = jugador["estadisticas"]
            print("Estadísticas del jugador seleccionado:")
            for clave, valor in estadisticas.items():
                print(f"{clave}: {valor}")
        else:
            print("Índice fuera de rango.")
    else:
        print("Entrada inválida. Debe ingresar un número.")
    """La función muestra por pantalla la lista de jugadores con sus índices correspondientes, pero no devuelve ningún valor."""

'''FUNCIONA'''#3 Función para guardar las estadísticas de un jugador en un archivo CSV
def guardar_estadisticas_csv(estadisticas: dict, nombre_archivo: str) -> None:
    campos = ["nombre", "posicion", "temporadas", "puntos_totales", "promedio_puntos_por_partido",
              "rebotes_totales", "promedio_rebotes_por_partido", "asistencias_totales",
              "promedio_asistencias_por_partido", "robos_totales", "bloqueos_totales",
              "porcentaje_tiros_de_campo", "porcentaje_tiros_libres", "porcentaje_tiros_triples"]

    with open(nombre_archivo, mode='w', newline='') as archivo:#with open para abrir el archivo en modo escritura ('w')
        escritor_csv = csv.DictWriter(archivo, fieldnames=campos)#se crea un objeto escritor_csv utilizando csv.DictWriter
        escritor_csv.writeheader() #writeheader() se utiliza para escribir la línea de encabezados en el archivo CSV
        escritor_csv.writerow(estadisticas) #writerow() para escribir las estadísticas del jugador en una nueva línea del archivo CSV      
    """La función guarda las estadísticas de un jugador en un archivo CSV, utilizando los campos definidos en la lista campos. No devuelve ningún valor, pero crea un archivo CSV con los datos proporcionados."""

def mostrar_lista_y_guardar_csv(lista: list) -> None:
    # Mostrar lista de jugadores con sus índices
    print("Lista de jugadores:")
    for i, jugador in enumerate(lista):
        print(f"{i+1}. {jugador['nombre']}")

    # Solicitar al usuario seleccionar un jugador por su índice
    seleccionado = input("Seleccione un jugador por su índice: ")

    if seleccionado.isdigit():
        indice = int(seleccionado) - 1
        if 0 <= indice < len(lista):
            jugador = lista[indice]
            estadisticas = jugador["estadisticas"]
            estadisticas["nombre"] = jugador["nombre"]  # Agregar el campo "nombre" a las estadísticas
            estadisticas["posicion"] = jugador["posicion"]

            guardar_csv = input("¿Desea guardar las estadísticas en un archivo CSV? (S/N): ")
            if guardar_csv.upper() == "S":
                nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
                guardar_estadisticas_csv(estadisticas, nombre_archivo)
                print(f"Las estadísticas se han guardado en el archivo {nombre_archivo}")
        else:
            print("Índice fuera de rango.")
    else:
        print("Entrada inválida. Debe ingresar un número.")
    """ La función muestra la lista de jugadores, permite al usuario seleccionar un jugador por su índice, guarda 
    las estadísticas del jugador en un archivo CSV si el índice es válido y devuelve mensajes informativos según las 
    acciones realizadas. No devuelve ningún valor."""

'''FUNCIONA'''#4 Función para buscar un jugador por su nombre
def buscar_jugador_por_nombre(lista: list, nombre: str) -> None:
    for jugador in lista:
        if jugador["nombre"].lower() == nombre.lower():
            print(f"Logros de {jugador['nombre']}:")
            for logro in jugador["logros"]:
                print(logro)
            return
    print(f"No se encontró ningún jugador con el nombre '{nombre}'.")
    """Busca un jugador por su nombre en la lista de jugadores e imprime sus logros si se encuentra.
    :param lista: Lista de jugadores.
    :param nombre: Nombre del jugador a buscar.
    :return: None"""
    
'''FUNCIONA'''#5 Función para calcular y mostrar el promedio de puntos por partido del equipo del Dream Team
def calcular_promedio_puntos_equipo(lista: list) -> None:
    # Crear una lista auxiliar para almacenar los nombres y promedios de puntos por partido
    promedios = []

    # Calcular el promedio de puntos por partido para cada jugador y agregarlo a la lista auxiliar
    for jugador in lista:
        nombre = jugador["nombre"]
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios.append((nombre, promedio_puntos))

    # Ordenar la lista de promedios por nombre utilizando el algoritmo de ordenamiento burbuja
    n = len(promedios)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if promedios[j][0] > promedios[j + 1][0]:
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]

    # Mostrar los promedios de puntos por partido del equipo ordenados por nombre
    print("Promedio de puntos por partido del equipo del Dream Team:")
    for nombre, promedio_puntos in promedios:
        print(f"{nombre}: {promedio_puntos}")
    """Calcula y muestra el promedio de puntos por partido para cada jugador en el equipo del Dream Team.
    :param lista: Lista de jugadores.
    :return: None"""

'''FUNCIONA'''#6 Función para verificar si un jugador es miembro del Salón de la Fama del Baloncesto
def verificar_miembro_salon_fama(nombre_jugador: str, lista: list) -> None:
    for jugador in lista:
        if jugador["nombre"] == nombre_jugador:
            if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                print(f"{nombre_jugador} es miembro del Salón de la Fama del Baloncesto.")
            else:
                print(f"{nombre_jugador} no es miembro del Salón de la Fama del Baloncesto.")
            return
    print(f"No se encontró ningún jugador con el nombre {nombre_jugador} en la lista.")
    """Verifica si un jugador es miembro del Salón de la Fama del Baloncesto.
    :param nombre_jugador: Nombre del jugador a verificar.
    :param lista: Lista de jugadores.
    :return: None """

'''FUNCIONA'''#7 Función para calcular y mostrar el jugador con la mayor cantidad de rebotes totales
def jugador_mayor_cantidad_rebotes(lista: list) -> None:    
    max_rebotes = 0
    jugador_max_rebotes = None

    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        rebotes_totales = estadisticas["rebotes_totales"]

        if rebotes_totales > max_rebotes:
            max_rebotes = rebotes_totales
            jugador_max_rebotes = jugador["nombre"]

    if jugador_max_rebotes is not None:
        print(f"El jugador con la mayor cantidad de rebotes totales es: {jugador_max_rebotes}")
        print(f"Cantidad de rebotes totales: {max_rebotes}")
    else:
        print("No se encontró ningún jugador en la lista.")
    """Encuentra el jugador con la mayor cantidad de rebotes totales en la lista y muestra su nombre y cantidad de rebotes.
    :param lista: Lista de jugadores.
    :return: None"""

'''FUNCIONA'''#8 Función para calcular y mostrar el jugador con el mayor porcentaje de tiros de campo
def jugador_mayor_porcentaje_tiros_campo(lista: list) -> None:
    max_porcentaje_tiros_campo = 0
    jugador_max_porcentaje_tiros_campo = None

    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        porcentaje_tiros_campo = estadisticas["porcentaje_tiros_de_campo"]

        if porcentaje_tiros_campo > max_porcentaje_tiros_campo:
            max_porcentaje_tiros_campo = porcentaje_tiros_campo
            jugador_max_porcentaje_tiros_campo = jugador["nombre"]

    if jugador_max_porcentaje_tiros_campo is not None:
        print(f"El jugador con el mayor porcentaje de tiros de campo es: {jugador_max_porcentaje_tiros_campo}")
        print(f"Porcentaje de tiros de campo: {max_porcentaje_tiros_campo}%")
    else:
        print("No se encontró ningún jugador en la lista.")
    """Encuentra el jugador con el mayor porcentaje de tiros de campo en la lista y muestra su nombre y porcentaje.
    :param lista: Lista de jugadores.
    :return: None"""

'''FUNCIONA'''#9 Función para calcular y mostrar el jugador con la mayor cantidad de asistencias totales
def jugador_mayor_asistencias_totales(lista: list) -> None:
    max_asistencias_totales = 0
    jugador_max_asistencias_totales = None

    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        asistencias_totales = estadisticas["asistencias_totales"]

        if asistencias_totales > max_asistencias_totales:
            max_asistencias_totales = asistencias_totales
            jugador_max_asistencias_totales = jugador["nombre"]

    if jugador_max_asistencias_totales is not None:
        print(f"El jugador con la mayor cantidad de asistencias totales es: {jugador_max_asistencias_totales}")
        print(f"Asistencias totales: {max_asistencias_totales}")
    else:
        print("No se encontró ningún jugador en la lista.")
    """Encuentra el jugador con la mayor cantidad de asistencias totales en la lista y muestra su nombre y cantidad de asistencias.
    :param lista: Lista de jugadores.
    :return: None"""

'''FUNCIONA'''#10 Función para filtrar jugadores por promedio de puntos por partido
def jugadores_promedio_puntos_superior(lista: list, valor: float) -> None:
    jugadores_superiores = []
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        promedio_puntos = estadisticas["promedio_puntos_por_partido"]

        if promedio_puntos > valor:
            jugadores_superiores.append(jugador["nombre"])

    if jugadores_superiores:
        print(f"Los jugadores que han promediado más puntos por partido que {valor} son:")
        for jugador in jugadores_superiores:
            print(jugador)
    else:
        print("No se encontraron jugadores con un promedio de puntos superior al valor ingresado.")
    """Identifica y muestra los jugadores cuyo promedio de puntos por partido es superior al valor dado.
    :param lista: Lista de jugadores.
    :param valor: Valor de referencia para comparar los promedios de puntos.
    :return: None"""

'''FUNCIONA'''#11 Función para filtrar jugadores por promedio de rebotes por partido
def jugadores_promedio_rebotes_superior(lista: list, valor: float) -> None:
    jugadores_superiores = []
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        promedio_rebotes = estadisticas["promedio_rebotes_por_partido"]

        if promedio_rebotes > valor:
            jugadores_superiores.append(jugador["nombre"])

    if jugadores_superiores:
        print(f"Los jugadores que han promediado más rebotes por partido que {valor} son:")
        for jugador in jugadores_superiores:
            print(jugador)
    else:
        print("No se encontraron jugadores con un promedio de rebotes superior al valor ingresado.")
    """Identifica y muestra los jugadores cuyo promedio de rebotes por partido es superior al valor dado.
    :param lista: Lista de jugadores.
    :param valor: Valor de referencia para comparar los promedios de rebotes.
    :return: None"""

'''FUNCIONA'''#12 Función para filtrar jugadores por promedio de asistencias por partido
def jugadores_promedio_asistencias_superior(lista: list, valor: float) -> None:
    jugadores_superiores = []
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        promedio_asistencias = estadisticas["promedio_asistencias_por_partido"]

        if promedio_asistencias > valor:
            jugadores_superiores.append(jugador["nombre"])

    if jugadores_superiores:
        print(f"Los jugadores que han promediado más asistencias por partido que {valor} son:")
        for jugador in jugadores_superiores:
            print(jugador)
    else:
        print("No se encontraron jugadores con un promedio de asistencias superior al valor ingresado.")
    """Identifica y muestra los jugadores cuyo promedio de asistencias por partido es superior al valor dado.
    :param lista: Lista de jugadores.
    :param valor: Valor de referencia para comparar los promedios de asistencias.
    :return: None"""

'''FUNCIONA'''#13 Función para calcular y mostrar el jugador con la mayor cantidad de robos totales
def jugador_mayor_cantidad_robos(lista) -> None:
    jugador_mayor_robos = None
    max_robos = 0
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        robos_totales = estadisticas["robos_totales"]

        if robos_totales > max_robos:
            max_robos = robos_totales
            jugador_mayor_robos = jugador["nombre"]

    if jugador_mayor_robos:
        print(f"El jugador con la mayor cantidad de robos totales es: {jugador_mayor_robos}")
        print(f"Cantidad de robos totales: {max_robos}")
    else:
        print("No se encontró ningún jugador en la lista.")
    """Encuentra el jugador con la mayor cantidad de robos totales en una lista de jugadores y sus estadísticas.
    :param lista: Lista de jugadores con sus estadísticas."""

'''FUNCIONA'''#14 Función para calcular y mostrar el jugador con la mayor cantidad de bloqueos totales
def jugador_mayor_cantidad_bloqueos(lista) -> None:
    jugador_mayor_bloqueos = None
    max_bloqueos = 0
    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        bloqueos_totales = estadisticas["bloqueos_totales"]

        if bloqueos_totales > max_bloqueos:
            max_bloqueos = bloqueos_totales
            jugador_mayor_bloqueos = jugador["nombre"]

    if jugador_mayor_bloqueos:
        print(f"El jugador con la mayor cantidad de bloqueos totales es: {jugador_mayor_bloqueos}")
        print(f"Cantidad de bloqueos totales: {max_bloqueos}")
    else:
        print("No se encontró ningún jugador en la lista.")
    """Encuentra al jugador con la mayor cantidad de bloqueos totales en una lista de jugadores y sus estadísticas.
    :param lista: Lista de jugadores con sus estadísticas.
    :return: None"""

'''FUNCIONA'''#15 Función para filtrar jugadores por porcentaje de tiros libres
def jugadores_por_porcentaje_tiros_libres(lista) -> None:
    valor_ingresado = float(input("Ingrese el valor de referencia para el porcentaje de tiros libres: "))
    jugadores_seleccionados = []

    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        porcentaje_tiros_libres = estadisticas["porcentaje_tiros_libres"]

        if porcentaje_tiros_libres > valor_ingresado:
            jugadores_seleccionados.append(jugador)

    if jugadores_seleccionados:
        print("Jugadores con porcentaje de tiros libres superior a", valor_ingresado)
        for jugador in jugadores_seleccionados:
            print("- Nombre:", jugador["nombre"])
            print("  Porcentaje de tiros libres:", jugador["estadisticas"]["porcentaje_tiros_libres"])
            print()
    else:
        print("No se encontraron jugadores con porcentaje de tiros libres superior a", valor_ingresado)
    """Selecciona los jugadores con un porcentaje de tiros libres superior a un valor de referencia dado.
    :param lista: Lista de jugadores con sus estadísticas.
    :return: None"""

'''FUNCIONA'''#16 Función para calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con menos puntos por partido
def promedio_puntos_sin_menor(lista) -> None:
    # Encontrar al jugador con la menor cantidad de puntos por partido
    jugador_menor_puntos = min(lista, key=lambda jugador: jugador["estadisticas"]["promedio_puntos_por_partido"])

    # Calcular el promedio de puntos excluyendo al jugador con la menor cantidad de puntos
    total_puntos = sum(jugador["estadisticas"]["promedio_puntos_por_partido"] for jugador in lista)
    total_jugadores = len(lista)
    promedio_puntos = (total_puntos - jugador_menor_puntos["estadisticas"]["promedio_puntos_por_partido"]) / (total_jugadores - 1)

    # Mostrar el promedio de puntos por partido
    print("Promedio de puntos por partido del equipo (excluyendo al jugador con la menor cantidad de puntos):", promedio_puntos)
    """Calcula el promedio de puntos por partido para una lista de jugadores, excluyendo al jugador con la menor cantidad de puntos.
    :param lista: Lista de jugadores con sus estadísticas.
    :return: None
    """

'''FUNCIONA'''#17 Función para calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
def jugador_con_mas_logros(lista) -> None:
    max_logros = 0
    jugador_mas_logros = None

    for jugador in lista:
        logros = len(jugador["logros"])
        if logros > max_logros:
            max_logros = logros
            jugador_mas_logros = jugador

    # Mostrar el jugador con la mayor cantidad de logros
    print("Jugador con la mayor cantidad de logros:")
    print("Nombre:", jugador_mas_logros["nombre"])
    print("Posición:", jugador_mas_logros["posicion"])
    print("Logros obtenidos:")
    for logro in jugador_mas_logros["logros"]:
        print("-", logro)
    """Encuentra al jugador con la mayor cantidad de logros en una lista de jugadores y muestra su información.
    :param lista: Lista de jugadores con sus logros.
    :return: None"""

'''FUNCIONA'''#18 Función para filtrar jugadores por porcentaje de tiros triples
def jugadores_con_porcentaje_triples_superior(lista, valor) -> None:
    jugadores_seleccionados = []

    for jugador in lista:
        porcentaje_triples = jugador["estadisticas"]["porcentaje_tiros_triples"]
        if porcentaje_triples > valor:
            jugadores_seleccionados.append(jugador)

    # Mostrar los jugadores con porcentaje de tiros triples superior al valor ingresado
    print("Jugadores con porcentaje de tiros triples superior a", valor, ":")
    if len(jugadores_seleccionados) == 0:
        print("No hay jugadores que cumplan con el criterio.")
    else:
        for jugador in jugadores_seleccionados:
            print("Nombre:", jugador["nombre"])
            print("Posición:", jugador["posicion"])
            print("Porcentaje de tiros triples:", jugador["estadisticas"]["porcentaje_tiros_triples"])
    """Encuentra y muestra los jugadores con porcentaje de tiros triples superior al valor ingresado.
    :param lista: Lista de jugadores con sus estadísticas.
    :param valor: Valor de referencia para el porcentaje de tiros triples.
    :return: None"""

'''FUNCIONA'''#19 Función para calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
def jugador_con_mas_temporadas(lista) -> None:
    jugador_mas_temporadas = None
    max_temporadas = 0
    for jugador in lista:
        temporadas = jugador["estadisticas"]["temporadas"]
        if temporadas > max_temporadas:
            max_temporadas = temporadas
            jugador_mas_temporadas = jugador

    # Mostrar el jugador con la mayor cantidad de temporadas jugadas
    if jugador_mas_temporadas is not None:
        print("Jugador con la mayor cantidad de temporadas jugadas:")
        print("Nombre:", jugador_mas_temporadas["nombre"])
        print("Posición:", jugador_mas_temporadas["posicion"])
        print("Temporadas jugadas:", jugador_mas_temporadas["estadisticas"]["temporadas"])
    else:
        print("No hay jugadores en la lista.")
    """Encuentra y muestra el jugador con la mayor cantidad de temporadas jugadas.
    :param lista: Lista de jugadores con sus estadísticas.
    :return: None"""

'''FUNCIONA'''#20 Función para filtrar jugadores por porcentaje de tiros de campo
def jugadores_por_porcentaje_tiros_de_campo(lista, valor) -> None:
    jugadores_filtrados = []

    for jugador in lista:
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if porcentaje_tiros_de_campo > valor:
            jugadores_filtrados.append(jugador)

    # Ordenar los jugadores por posición en la cancha
    jugadores_ordenados = sorted(jugadores_filtrados, key=lambda j: j["posicion"])

    # Mostrar la información de los jugadores filtrados y ordenados
    if jugadores_ordenados:
        print("Jugadores con un porcentaje de tiros de campo superior a", valor)
        for jugador in jugadores_ordenados:
            print("Nombre:", jugador["nombre"])
            print("Posición:", jugador["posicion"])
            print("Porcentaje de tiros de campo:", jugador["estadisticas"]["porcentaje_tiros_de_campo"])
            print("--------------------")
    else:
        print("No hay jugadores que cumplan el criterio.")
    """Filtra y muestra los jugadores con un porcentaje de tiros de campo superior a un valor dado, ordenados por posición.
    :param lista: Lista de jugadores con sus estadísticas.
    :param valor: Valor de referencia para el porcentaje de tiros de campo.
    :return: None"""

'''FUNCIONA'''#21Bonus
def calcular_posiciones_rankings(lista) -> None:
    rankings = {
        "Puntos": [],
        "Rebotes": [],
        "Asistencias": [],
        "Robos": []
    }

    for jugador in lista:
        nombre = jugador["nombre"]
        puntos = jugador["estadisticas"]["puntos_totales"]
        rebotes = jugador["estadisticas"]["rebotes_totales"]
        asistencias = jugador["estadisticas"]["asistencias_totales"]
        robos = jugador["estadisticas"]["robos_totales"]

        rankings["Puntos"].append((nombre, puntos))
        rankings["Rebotes"].append((nombre, rebotes))
        rankings["Asistencias"].append((nombre, asistencias))
        rankings["Robos"].append((nombre, robos))

    # Ordenar los rankings en base a los valores
    for ranking in rankings.values():
        ranking.sort(key=lambda x: x[1], reverse=True)

    # Crear archivo CSV y escribir los rankings
    with open("rankings.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Puntos", "Rebotes", "Asistencias", "Robos"])

        for i in range(len(lista)):
            row = [rankings["Puntos"][i][0], rankings["Rebotes"][i][0], rankings["Asistencias"][i][0], rankings["Robos"][i][0]]
            writer.writerow(row)

    print("Archivo CSV exportado exitosamente.")
    """Calcula los rankings de puntos, rebotes, asistencias y robos para una lista de jugadores y exporta los resultados
    a un archivo CSV.
    :param lista: Lista de jugadores con sus estadísticas.
    :return: None
    """

'''FUNCIONA'''#22 Determinar la cantidad de jugadores que hay por cada posición.
def contar_jugadores_por_posicion(lista):
    jugadores_por_posicion = {}

    for jugador in lista:
        posicion = jugador["posicion"]
        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion] += 1
        else:
            jugadores_por_posicion[posicion] = 1

    return jugadores_por_posicion
    #Esta función recibe una lista de jugadores y cuenta la cantidad de jugadores por posición.
    #Recibe un parámetro - Lista: una lista de diccionarios que representan jugadores donde cada uno tiene una clave "posición" que indica su posición.
    #Retorna un diccionario donde las claves son las posiciones y los valores son la cantidad de jugadores que tienen la esa posición.

'''FUNCIONA'''#23 Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.
def obtener_cantidad_jugadores_por_all_star(jugador):
    for logro in jugador["logros"]:
        if "All-Star" in logro:
            cantidad_all_star = logro.split(" ")[0]
            cantidad_all_star = int(cantidad_all_star)
            return cantidad_all_star 
    return 0
    #Esta función recibe una lista de jugadores y los ordena en función de la cantidad de veces que han sido seleccionados como All-Star.
    #Imprime el nombre del jugador seguido a la cantidad de veces que ha sido All Star en orden descendente.
    #Recibe un parámetro - Lista: una lista de diccionario que representan jugadores donde cada uno tiene una clave "logros" que contiene esa lista donde se encuentra la cantidad de veces que han sido All-Star
    #No retorna ningun valor.

'''FUNCIONA'''#24 Determinar qué jugador tiene las mejores estadísticas en cada valor.
def obtener_mejores_estadisticas(lista):
    mejores_estadisticas = {}

    for jugador in lista:
        nombre = jugador["nombre"]
        estadisticas = jugador["estadisticas"]

        for estadistica, valor in estadisticas.items():
            if estadistica not in mejores_estadisticas or valor > mejores_estadisticas[estadistica][1]:
                mejores_estadisticas[estadistica] = (nombre, valor)

    for estadistica, mejor_jugador in mejores_estadisticas.items():
        nombre_jugador = mejor_jugador[0]
        valor_estadistica = mejor_jugador[1]
        print(f"Mayor cantidad de {estadistica}: {nombre_jugador} ({valor_estadistica})")

'''FUNCIONA'''#25 Determinar qué jugador tiene las mejores estadísticas de todos.
def obtener_mejores_estadisticas_totales(lista):
    mejor_jugador = None

    for jugador in lista:
        nombre = jugador["nombre"]
        estadisticas = jugador["estadisticas"]

        if mejor_jugador is None or sum(estadisticas.values()) > sum(mejor_jugador["estadisticas"].values()):
            mejor_jugador = jugador

    if mejor_jugador is not None:
        nombre_jugador = mejor_jugador["nombre"]
        print(f"Mejor jugador: {nombre_jugador}")
        print("Estadísticas:")
        for estadistica, valor in mejor_jugador["estadisticas"].items():
            print(f"{estadistica}: {valor}")
    else:
        print("No se encontraron jugadores en la lista.")

#Menu a partir de una lista de opciones
def generar_menu(lista: list) -> int:
    for opcion in lista:
        print(opcion)

    opcion_elegida = int(input("\nElija una opcion: "))
    print()

    return opcion_elegida
"""Genera un menú a partir de una lista de opciones y solicita al usuario que elija una opción.
:param lista: Lista de opciones.
:return: El número de opción elegido por el usuario."""

# Función para mostrar el menú de opciones y procesar la elección del usuario
def mostrar_menu():
    continuar = True

    while continuar == True:

        opcion_menu = generar_menu(lista_menu)

        match opcion_menu:
            case 1:
                print("\n------ Lista de jugadores del Dream Team ------")
                mostrar_lista_jugadores(lista_jugadores)
            case 2:
                mostrar_estadisticas_jugador(lista_jugadores)
            case 3:
                mostrar_lista_y_guardar_csv(lista_jugadores) 
            case 4:
                nombre_buscar = input("Ingrese el nombre del jugador a buscar: ")
                buscar_jugador_por_nombre(lista_jugadores, nombre_buscar)
            case 5:
                calcular_promedio_puntos_equipo(lista_jugadores)
            case 6:
                nombre_ingresado = input("Ingrese el nombre de un jugador: ")
                verificar_miembro_salon_fama(nombre_ingresado, lista_jugadores)
            case 7:
                jugador_mayor_cantidad_rebotes(lista_jugadores)
            case 8:
                jugador_mayor_porcentaje_tiros_campo(lista_jugadores)
            case 9:
                jugador_mayor_asistencias_totales(lista_jugadores)
            case 10:
                valor = float(input("Ingrese un valor de promedio de puntos por partido: "))
                jugadores_promedio_puntos_superior(lista_jugadores, valor)
            case 11:
                valor = float(input("Ingrese un valor de promedio de rebotes por partido: "))
                jugadores_promedio_rebotes_superior(lista_jugadores, valor)
            case 12:
                valor = float(input("Ingrese un valor de promedio de asistencias por partido: "))
                jugadores_promedio_asistencias_superior(lista_jugadores, valor)
            case 13:
                jugador_mayor_cantidad_robos(lista_jugadores)
            case 14:
                jugador_mayor_cantidad_bloqueos(lista_jugadores)
            case 15:
                jugadores_por_porcentaje_tiros_libres(lista_jugadores)
            case 16:
                promedio_puntos_sin_menor(lista_jugadores)
            case 17:
                jugador_con_mas_logros(lista_jugadores)
            case 18:
                valor_ingresado = float(input("Ingrese el valor del porcentaje de tiros triples: "))
                jugadores_con_porcentaje_triples_superior(lista_jugadores, valor_ingresado)
            case 19:
                jugador_con_mas_temporadas(lista_jugadores)
            case 20:
                valor_ingresado = float(input("Ingrese un valor para el porcentaje de tiros de campo: "))
                jugadores_por_porcentaje_tiros_de_campo(lista_jugadores, valor_ingresado)
            case 21:
                calcular_posiciones_rankings(lista_jugadores)
            case 22:
                jugadores_por_posicion = contar_jugadores_por_posicion(lista_jugadores)
                for posicion, cantidad in jugadores_por_posicion.items():
                    print(f"{posicion}: {cantidad}")
            case 23:
                jugadores_ordenados = sorted(lista_jugadores, key=obtener_cantidad_jugadores_por_all_star, reverse=True)
                for jugador in jugadores_ordenados:
                    cantidad_all_star = obtener_cantidad_jugadores_por_all_star(jugador)
                    print(f"Nombre: {jugador['nombre']}")
                    print(f"All-Star: {cantidad_all_star}")
            case 24:
                obtener_mejores_estadisticas(lista_jugadores)
            case 25:
                obtener_mejores_estadisticas_totales(lista_jugadores)
            case 26:
                print("¡Hasta luego!")
                continuar = False
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")

        input('\nPresione cualquier tecla para continuar. \n')
    """Muestra un menú interactivo en el que el usuario puede seleccionar diferentes opciones y realizar acciones relacionadas
    con la lista de jugadores."""

lista_menu = [
            "\n\t--- Menú de Opciones ---\n",
            "1. Mostrar lista de jugadores del Dream Team",
            "2. Mostrar estadísticas completas de un jugador",
            "3. Guardar estadísticas de un jugador en archivo CSV",
            "4. Buscar jugador por nombre",
            "5. Calcular y mostrar el promedio de puntos por partido del equipo",
            "6. Verificar si un jugador es miembro del Salón de la Fama del Baloncesto",
            "7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales",
            "8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo",
            "9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales",
            "10. Filtrar jugadores por promedio de puntos por partido",
            "11. Filtrar jugadores por promedio de rebotes por partido",
            "12. Filtrar jugadores por promedio de asistencias por partido",
            "13. Calcular y mostrar el jugador con la mayor cantidad de robos totales",
            "14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales",
            "15. Filtrar jugadores por porcentaje de tiros libres",
            "16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con menos puntos por partido",
            "17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos",
            "18. Filtrar jugadores por porcentaje de tiros triples",
            "19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas",
            "20. Filtrar jugadores por porcentaje de tiros de campo",
            "21. Bonus",
            "22. Determinar la cantidad de jugadores que hay por cada posición.",
            "23. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.",
            "24. Determinar qué jugador tiene las mejores estadísticas en cada valor.",
            "25. Determinar qué jugador tiene las mejores estadísticas de todos.",
            "26. Salir del programa"
        ]

# Ejecutar el programa
lista_jugadores = parse_json_jugadores(r"PARCIAL\dt.json")
mostrar_menu()
