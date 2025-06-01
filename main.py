import json
import random
from datetime import datetime

def mostrarHistorial(historial):
    try:
        with open(historial, "r", encoding="utf-8") as archivo:
            print("\n📖 HISTORIAL DE PARTIDAS")
            print("────────────────────────────")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("⚠️ No hay historial guardado aún.")

def actualizarHistorial(nombre, palabraSecreta, errores, dificultad, gano, fecha_hora):
    try:
        with open("historial_partidas.txt", "a", encoding="utf-8") as archivo:
            linea = (
                f"Jugador: {nombre}\n"
                f"Dificultad: {dificultad}\n"
                f"Resultado: {'Ganó' if gano else 'Perdió'}\n"
                f"Palabra secreta: {palabraSecreta.upper()}\n"
                f"Intentos usados: {errores}\n"
                f"Fecha y hora: {fecha_hora}\n"
                "────────────────────────────\n"
            )
            archivo.write(linea)
        return "historial_partidas.txt"
    except Exception as e:
        print(f"Ocurrio un error: {e}")

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
    return palabraDeUsuario == palabraSecreta

def generarPistas(palabraDeUsuario, palabraSecreta):
    palabraDeUsuario = list(palabraDeUsuario)
    palabraSecreta = list(palabraSecreta)
    copiaPalabraSecreta = list(palabraSecreta)
    pistas = ["⬜"] * len(palabraSecreta)
    
    for i in range(len(palabraSecreta)):
        if palabraDeUsuario[i] == palabraSecreta[i]:
            pistas[i] = "🟩"
            copiaPalabraSecreta[i] = "_"
    for i in range(len(palabraSecreta)):
        if pistas[i] == "⬜" and palabraDeUsuario[i] in copiaPalabraSecreta:
            pistas[i] = "🟨"
            idx = copiaPalabraSecreta.index(palabraDeUsuario[i])
            copiaPalabraSecreta[idx] = "_"
    return pistas

def estaEnElDiccionario(palabras, palabraDeUsuario):
    return palabraDeUsuario in palabras

def ingresarPalabra(longitud):
    try:
        palabraDeUsuario = str(input(f"Ingrese una palabra de {longitud} letras:")).lower()
        while len(palabraDeUsuario) != longitud or not palabraDeUsuario.isalpha():
            print(f"❌ La palabra debe tener exactamente {longitud} letras. Volvé a intentarlo.")
            palabraDeUsuario = str(input(f"Ingrese una palabra de {longitud} letras:")).lower()
        return palabraDeUsuario
    except Exception as e:
        print(f"Ocurrio un error: {e}")  

def generarPalabraSecreta(palabras):
    try:
        palabraSecreta = random.choice(palabras)
        return palabraSecreta
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    
def generarListasDePalabras(dificultad):
    try:
        with open("palabras_wordle.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            
            if dificultad == 1:
                longitud = 5
                intentos = 7
                palabras = data[str(longitud)]
            elif dificultad == 2:
                longitud = 6
                intentos = 6 
                palabras = data[str(longitud)]   
            else:
                longitud = 7
                intentos = 5
                palabras = data[str(longitud)]  
        return palabras, longitud, intentos
    except Exception as e:
        print(f"Ocurrio un error: {e}")     
        
def elegirDificultad(): 
    print("────────────────────────────────")
    print("🧠 Elegí un nivel de dificultad: ")
    print("1️⃣  Fácil → Palabras de 5 letras (más intentos)")
    print("2️⃣  Medio → Palabras de 6 letras")
    print("3️⃣  Difícil → Palabras de 7 letras (menos intentos)")
    print("💬 Ingresá 1, 2 o 3 según el nivel que quieras jugar.")
    print("────────────────────────────────")

    try:
        dificultad = int(input("Ingresa la dificultad con la que desea jugar: "))
        while dificultad not in [1, 2, 3]:
            print("🤷‍♂️ Esa opción no es válida. Tenés que elegir entre 1 (Fácil), 2 (Medio) o 3 (Difícil). ¡Intentá de nuevo!")
            dificultad = int(input("Ingresa la dificultad con la que desea jugar: "))
        return dificultad
    except Exception as e:
        print(f"Ocurrio un error: {e}") 

def darBienvenida():
    try:   
        nombre = input("Ingresa tu nombre: ").lower()
        while nombre.strip() == "" or not nombre.isalpha():
            print("🤓 El nombre debe contener solo letras (sin números ni símbolos). ¡Volvé a intentarlo!")
            nombre = input("Ingresa tu nombre: ").lower()
        return nombre
    except Exception as e:
        print(f"Ocurrio un error: {e}")   
        
def main():
    nombre = darBienvenida()
    print(f"🧠 {nombre.capitalize()}, ¿listo para jugar? Elegí tu nivel de dificultad y a jugar.")
    
    partidasJugadas = 0
    partidasGanadas = 0
    partidasPerdidas = 0

    while True:
        dificultad = elegirDificultad()
        palabras, longitud, intentos = generarListasDePalabras(dificultad)
        palabraSecreta = generarPalabraSecreta(palabras)

        errores = 0
        ganador = False

        print("\n🎮 Nueva partida iniciada. ¡Buena suerte!\n")
        partidasJugadas += 1

        while errores < intentos and not ganador:
            palabraDeUsuario = ingresarPalabra(longitud)
            existe = estaEnElDiccionario(palabras, palabraDeUsuario)
            pistas = generarPistas(palabraDeUsuario, palabraSecreta)
            print(f"📝 Tu intento: {palabraDeUsuario.upper()}")
            print("👉 Resultado: " + "".join(pistas))

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
            
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        historial = actualizarHistorial(nombre, palabraSecreta, errores, dificultad, ganador, fecha_hora)

        if not continuarJugando():
            print("\n📊 RESUMEN DE LA PARTIDA")
            print("────────────────────────────")
            print(f"🎮 Partidas jugadas: {partidasJugadas}")
            print(f"🏆 Partidas ganadas: {partidasGanadas}")
            print(f"💀 Partidas perdidas: {partidasPerdidas}")
            print("🙌 ¡Gracias por jugar a Wordle en Python!")
            print("Volvé pronto para poner a prueba tu vocabulario. 😄")
            mostrarHistorial(historial)
            break
main()    