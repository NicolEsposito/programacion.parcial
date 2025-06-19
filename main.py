from inputs import leer_nombre, leer_entero, leer_opcion_menu
from funciones import *

# programa principal
nombres = []    # Lista de nombres de participantes
notas = []      # Lista de listas con notas por jurado
promedios = []  # Lista de promedios por participante

while True:
    print("\n======= MENU =======")
    print("1. Cargar participantes")
    print("2. Cargar puntajes")
    print("3. Mostrar datos")
    print("4. Promedios mayores a 4")
    print("5. Promedios mayores a 7")
    print("6. promedio de cada jurado")
    print("7. menor puntaje por jurado")
    print("8. buscar participante por nombre")
    print("9. Mostrar top 3")
    print("10. Ordenar alfabéticamente")
    print("11. mostrar ganador")
    print("12. desempatar")
    print("0. salir")

    opcion = leer_opcion_menu("Elija una opción: ")
    print(" ")

    if opcion == "1":    # Carga los nombres de los participantes
        print("Opcion: 1")
        nombres = cargar_nombres()
    elif opcion == "2": 


        print("Opcion: 2")
        if nombres:  # Carga las notas de cada jurado por participante y calcula sus promedios
            notas = cargar_notas(nombres)
            promedios = calcular_promedios(notas)
        else:
            print("Debe cargar los participantes primero.")
    elif opcion == "3":


        print("Opcion: 3")
        if notas and promedios:  # Imprime todos los datos
            imprimir_todo(nombres, notas, promedios)
        else:
            print("Debe cargar los puntajes primero.")
    elif opcion == "4":


        print("Opcion: 4")
        if promedios:    # Filtra promedios mayores a 4
            indices = filtrar_promedios(promedios, lambda x: x > 4)
            if indices:
                for i in indices:
                    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f}")
            else:
                print("Ningún participante supera el promedio de 4.")
        else:
            print("Debe cargar los puntajes primero.")
    elif opcion == "5":


        print("Opcion: 5")
        if promedios:    # Filtra promedios mayores a 7
            indices = filtrar_promedios(promedios, lambda x: x > 7)
            if indices:
                for i in indices:
                    print(f"{nombres[i]} - Promedio: {promedios[i]:.2f}")
            else:
                print("Ningún participante tiene promedio mayor a 4.")
        else:
            print("Debe cargar los puntajes primero.")
    elif opcion == "6":


        print("Opcion: 6") #Mostrar el promedio de puntajes otorgados por cada jurado
        if notas:
             promedios_jurado = promedio_por_jurado(notas)
             for j, promedio in enumerate(promedios_jurado):
                print(f"Promedio del Jurado {j+1}: {promedio}/10")
        else:
            print("Debe cargar los puntajes primero.")
    elif opcion == "7":


        print("Opcion: 7") #Mostrar el menor puntaje otorgado por cada jurado
        if notas:
            minimos = minimos_por_columna(notas)
            for j, m in enumerate(minimos):
                print(f"Jurado {j+1} menor puntaje: {m}")
        else:
            print("Debe cargar los puntajes primero.")
    elif opcion == "8":

        print("Opción: 8") #Busca un participante por su nombre y mostrar sus datos si existe
        if nombres and notas and promedios:
            nombre_buscado = leer_nombre("Ingrese el nombre del participante a buscar: ")
            buscar_participante(nombre_buscado, nombres, notas, promedios)
        else:
            print("Debe cargar los participantes y puntajes primero.")

    elif opcion == "9":
        print("Opcion: 9")
        if promedios:    # Muestra el top 3 de promedios
            top_nombres, top_promedios = obtener_top3(nombres, promedios)
            print("Top 3 participantes:")
            for i in range(len(top_nombres)):
                print(f"{i+1}. {top_nombres[i]} - Promedio: {top_promedios[i]:.2f}")
        else:
            print("Debe cargar los participantes y puntajes primero.")

    elif opcion =="10":
        if nombres and notas and promedios:  # Ordena los participantes alfabéticamente
            ordenar_por_nombre(nombres, notas, promedios)
            print("Participantes ordenados alfabéticamente:")
            imprimir_todo(nombres, notas, promedios)
        else:
            print("Debe cargar los participantes y puntajes primero.")

    elif opcion == "11":
            print("Opción: 11") #Muestra al participante ganador con el mayor promedio
            if promedios:
                ganadores = obtener_ganadores(nombres, promedios)
            if len(ganadores) == 1:
                print(f"El ganador es: {ganadores[0]}")
            elif len(ganadores) > 1:
                print("Hay un empate entre los siguientes participantes:")
                for g in ganadores:
                    print(f"- {g}")
                print("Debe realizar un desempate (opción 12).")
            else:
                print("No se encontraron ganadores.")

    elif opcion == "12":
        print("Opción: 12") #Resuelve el empate entre ganadores eligiendo uno al azar
        if promedios:
            ganadores = obtener_ganadores(nombres, promedios)
            if len(ganadores) > 1:
                desempatar(ganadores)
            else:
                print("No hay empate. No es necesario desempatar.")
        else:
            print("Debe cargar los puntajes primero.")

    elif opcion == "0":   
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")