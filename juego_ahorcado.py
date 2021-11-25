import random
import time

def palabras():
    with open("./lista_juego_del_ahorcado.txt") as archivo:
        palabras = archivo.readlines()
    palabras = [x.strip() for x in palabras]
    return palabras


def run():
    print("Bienvenido al juego del ahorcado")
    time.sleep(2)
    print("Intenta adivinar que palabra hay")
    time.sleep(2)
    print("Cuentas con cinco vidas para este juego. Si te equivocas cinco veces. Pierdes")
    print("Empecemos el juego")
    jugador = input("Ingresa tu nombre: ")
    print("Hola " + jugador + "!")
    time.sleep(2)
    print("Empieza el juego")
    time.sleep(2)
    palabra_secreta = random.choice(palabras())
    print(palabra_secreta)
    if palabra_secreta == "":
        print("No se pudo encontrar la palabra")
        return
    letras_acertadas = ["_" for letra in palabra_secreta]
    print(letras_acertadas)
    intentos = 0
    while intentos < 5:
        letra = input("Ingrese una letra: ")
        if letra in palabra_secreta:
            print("La letra esta en la palabra")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_acertadas[i] = letra
            print(letras_acertadas)
        else:
            print("La letra no esta en la palabra")
            intentos += 1
            print("Te quedan " + str(5 - intentos) + " intentos")
        if "_" not in letras_acertadas:
            print("Felicidades, ganaste")
            break
    if intentos == 5:
        print("Perdiste, la palabra era " + palabra_secreta)
        


if __name__ == "__main__":
    run()