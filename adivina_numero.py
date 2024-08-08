import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado  = False

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre el 1 y el 100.")

    while not adivinado:
        try:
            intento = int(input("Adivina el número: "))
            intentos += 1

            if intento < numero_secreto:
                print("Demasiadom bajo. Intentalo de nuevo")

            elif intento > numero_secreto:
                print("Demasiado alto. Prueba otra vez")
        
            else:
                print(f"¡Correcto! acertastes en {intentos} intentos.")

        except ValueError:
            print("Error: Por favor, introduce un número válido.")
        
adivina_el_numero()