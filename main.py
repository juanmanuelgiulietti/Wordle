import os
import random

def continuarJugando():
    try:
        continuar = str(input("¿Querés jugar otra vez? (s/n)")).lower()
        while continuar not in ["s", "n"]:
            print("❌ Entrada inválida. Por favor, escribí S para sí o N para no.")
            continuar = str(input("¿Querés jugar otra vez? (s/n)")).lower()
            
        if continuar == "s":
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        
def determinarResultado(palabraDeUsuario, palabraSecreta):
    ganador = False
    if palabraDeUsuario == palabraSecreta:
        ganador = True
    else:
        ganador = False
    return ganador

def generarPistas(palabraDeUsuario, palabraSecreta):
    palabraDeUsuario = list(palabraDeUsuario)
    palabraSecreta = list(palabraSecreta)
    copiaPalabraSecreta = list(palabraSecreta)
    pistas = ["⬜"] * 5
    
    for i in range(5):
        if palabraDeUsuario[i] == palabraSecreta[i]:
            pistas[i] = "🟩"
            copiaPalabraSecreta[i] = "_"
    for i in range(5):
        if pistas[i] == "⬜" and palabraDeUsuario[i] in copiaPalabraSecreta:
            pistas[i] = "🟨"
            idx = copiaPalabraSecreta.index(palabraDeUsuario[i])
            copiaPalabraSecreta[idx] = "_"
    return pistas

def estaEnElDiccionario(palabras, palabraDeUsuario):
    return palabraDeUsuario in palabras

def ingresarPalabra():
    try:
        palabraDeUsuario = str(input("Ingrese una palabra de 5 letras: ")).lower()
        while len(palabraDeUsuario) != 5 or not palabraDeUsuario.isalpha():
            print("❌ La palabra debe tener exactamente 5 letras. Volvé a intentarlo.")
            palabraDeUsuario = str(input("Ingrese una palabra de 5 letras: ")).lower()
        return palabraDeUsuario
    except Exception as e:
        print(f"Ocurrio un error: {e}")  

def generarPalabraSecreta():
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual, archivoPalabras)
    
    try:
        with open(rutaArchivo, "r") as archivo:
            palabras = []
            for palabra in archivo:
                palabras.append(palabra.strip())
            palabraSecreta = random.choice(palabras) 
            return palabras, palabraSecreta
    except Exception as e:
        print(f"Ocurrio un error: {e}")       
        
def main():
    partidasJugadas = 0
    partidasGanadas = 0
    partidasPerdidas = 0

    while True:
        palabras, palabraSecreta = generarPalabraSecreta()

        errores = 0
        intentos = 6
        ganador = False

        print("\n🎮 Nueva partida iniciada. ¡Buena suerte!\n")
        partidasJugadas += 1

        while errores < intentos and not ganador:
            palabraDeUsuario = ingresarPalabra()
            existe = estaEnElDiccionario(palabras, palabraDeUsuario)
            pistas = generarPistas(palabraDeUsuario, palabraSecreta)
            print("👉 Resultado: " +  "".join(pistas))

            if existe:
                ganador = determinarResultado(palabraDeUsuario, palabraSecreta)
                if ganador:
                    print(f"🎉 ¡Correcto! Adivinaste la palabra secreta: {palabraSecreta.upper()}")
                if not ganador:
                    errores += 1
                    print("❌ No es la palabra secreta.")
                    print(f"❗ Intentos restantes: {intentos - errores}\n")
            else:
                errores += 1
                print(f"❗ Intentos restantes: {intentos - errores}\n")

        if ganador:
            partidasGanadas += 1
        else:
            print(f"💀 Te quedaste sin intentos. La palabra era: {palabraSecreta.upper()}")
            partidasPerdidas += 1

        if not continuarJugando():
            print("\n📊 RESUMEN DE LA PARTIDA")
            print("────────────────────────────")
            print(f"🎮 Partidas jugadas: {partidasJugadas}")
            print(f"🏆 Partidas ganadas: {partidasGanadas}")
            print(f"💀 Partidas perdidas: {partidasPerdidas}")
            print("🙌 ¡Gracias por jugar a Wordle en Python!")
            print("Volvé pronto para poner a prueba tu vocabulario. 😄")
            break
main()    