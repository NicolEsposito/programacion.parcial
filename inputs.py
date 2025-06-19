def leer_entero(mensaje, minimo=1, maximo=10):
#Solicita al usuario ingresar un número entero dentro de un rango especificado.

    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


# Solicita al usuario ingresar un nombre válido (mínimo 3 letras, solo alfabético).
# Requisitos del nombre:
#       - Debe contener al menos 3 caracteres.
#       - Puede contener espacios pero solo letras (sin números ni símbolos).
def leer_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if len(nombre) >= 3 and nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("Nombre inválido. Debe tener al menos 3 letras y solo contener caracteres alfabéticos.")
#  Solicita al usuario una opción del menú, sin validación adicional.
def leer_opcion_menu(mensaje):
    return input(mensaje).strip()