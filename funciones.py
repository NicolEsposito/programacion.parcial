from inputs import leer_nombre, leer_entero
import random 

# Solicita al usuario ingresar los nombres de los participantes y Retorna una lista de nombres.
def cargar_nombres():
    nombres = []
    contador = 0
    while contador < 5:
        nombre = input(f"Participante #{contador + 1}: ").strip()
        if len(nombre) >= 3 and nombre.replace(" ", "").isalpha():
            nombres += [nombre]
            contador += 1
        else:
            print("Nombre inválido. Mínimo 3 letras y solo caracteres alfabéticos.")
    return nombres

# función para ingresar 3 notas por participante y Solicita las notas dadas por jurados a cada participante.
# y Retorna una lista de listas con las notas por participante.
def cargar_notas(nombres):
    notas = []
    for nombre in nombres:
        fila = []
        jurado = 0
        while jurado < 3:
            try:
                nota = int(input(f"Nota de jurado #{jurado+1} para {nombre}: "))
                if 1 <= nota <= 10:
                    fila += [nota]
                    jurado += 1
                else:
                    print("La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Ingrese un número válido.")
        notas += [fila]
    return notas


nombres = []
notas = []

def promedio_fila(fila): #Calcula el promedio de una lista de notas.
    suma = 0
    for nota in fila:
        suma += nota
    return suma / len(fila)

def calcular_promedios(matriz): #Calcula los promedios por participante.
    resultados = []
    for fila in matriz:
        promedio = promedio_fila(fila)
        resultados.append(promedio)
    return resultados

def imprimir_todo(nombres, notas, promedios): #Imprime los nombres, notas y promedios de todos los participantes.
    for i in range(len(nombres)):
        print("\nNOMBRE DEL PARTICIPANTE:", nombres[i])
        for j in range(len(notas[i])):
            print(f" PUNTAJE DEL JURADO {j+1}: {notas[i][j]}")
        print("PROMEDIO:", round(promedios[i], 2,),"/10")

def filtrar_promedios(promedios, condicion): #Filtra los índices cuyos promedios cumplen cierta condición.
    indices = []
    for i in range(len(promedios)):
        if condicion(promedios[i]):
            indices.append(i)
    return indices

def minimos_por_columna(matriz):
    # Inicializa con los primeros valores de cada columna
    minimos = [matriz[0][0], matriz[0][1], matriz[0][2]]
    for j in range(3):  # 3 jurados
        for i in range(len(matriz)):  # participantes
            if matriz[i][j] < minimos[j]:
                minimos[j] = matriz[i][j]
    return minimos   

def promedio_por_jurado(matriz): #Calcula el promedio de cada jurado (columna).
    cantidad_jurados = len(matriz[0])
    cantidad_participantes = len(matriz)
    promedios = []

    for j in range(cantidad_jurados):
        suma = 0
        for i in range(cantidad_participantes):
            suma += matriz[i][j]
        promedio = suma / cantidad_participantes
        promedios.append(round(promedio, 2))
    
    return promedios

def buscar_participante(nombre_buscado, nombres, notas, promedios): #busca el nombre ingresado y muestra sus datos
    for i, nombre in enumerate(nombres):
        if nombre.lower() == nombre_buscado.lower():
            print("\nParticipante encontrado:")
            print(f"Nombre: {nombre}")
            for j, nota in enumerate(notas[i]):
                print(f"Nota jurado {j+1}: {nota}")
            print(f"Promedio: {round(promedios[i], 2)} / 10")
            return
    print("Participante no encontrado.")


# Obtiene el top 3 de participantes con los mejores promedios.
def obtener_top3(nombres, promedios):
    nombres_copia = nombres[:]
    promedios_copia = promedios[:]
    for i in range(len(promedios_copia)):
        for j in range(i + 1, len(promedios_copia)):
            if promedios_copia[i] < promedios_copia[j]:
                promedios_copia[i], promedios_copia[j] = promedios_copia[j], promedios_copia[i]
                nombres_copia[i], nombres_copia[j] = nombres_copia[j], nombres_copia[i]
    return nombres_copia[:3], promedios_copia[:3]

# Ordena los participantes alfabéticamente junto con sus notas y promedios.
def ordenar_por_nombre(nombres, notas, promedios):
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i] > nombres[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                notas[i], notas[j] = notas[j], notas[i]
                promedios[i], promedios[j] = promedios[j], promedios[i]

def obtener_ganadores(nombres, promedios): #Obtiene una lista de participantes con el promedio más alto.
    if not promedios:
        return []
    max_promedio = max(promedios)
    ganadores = [nombres[i] for i in range(len(promedios)) if promedios[i] == max_promedio]
    return ganadores

def desempatar(ganadores): #Realiza un desempate eligiendo aleatoriamente a uno de los ganadores en caso de empate.
    if not ganadores:
        print("No hay ganadores para desempatar.")
        return

    ganador = random.choice(ganadores)
    print(f"Ganador elegido por desempate: {ganador}")

