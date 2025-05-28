import os
import random

def empezarJuego(archivo):
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual, archivo)
    
    try:
        with open(rutaArchivo, "r") as archivoLectura:
            palabras = [palabra.strip().lower() for palabra in archivoLectura]
             
            palabraSecreta = random.choice(palabras)
             
            intentos = 6
            errores = 0
            ganador = False
            
            while errores < intentos and not ganador:
                palabraIngresada = str(input("🔤 Ingrese una palabra de 5 letras: ")).lower()
                while len(palabraIngresada) != 5:
                    print("❌ Palabra inválida. Acordate que debe tener exactamente 5 letras.")
                    palabraIngresada = str(input("🔤 Ingrese una palabra de 5 letras: ")).lower()
                
                if palabraIngresada not in palabras:
                    print("🚫 Esa palabra no está en el diccionario.")
                    errores += 1
                    print(f"❗ Intentos restantes: {intentos - errores}")
                    continue
             
                if palabraIngresada == palabraSecreta:
                    print(f"🎉 ¡Correcto! Adivinaste la palabra secreta: {palabraSecreta.upper()}")
                    ganador = True
                else:
                    print("❌ No es la palabra secreta.")
                    errores += 1
                    print(f"❗ Intentos restantes: {intentos - errores}")
                    
            if not ganador:
                print(f"💀 Te quedaste sin intentos. La palabra era: {palabraSecreta.upper()}")
             
    except Exception as e:
        print(f"Ocurrio un error: {e}")    

def prepararPartida(archivo):
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual, archivo)
    
    try:
        with open(rutaArchivo, "r") as archivo:
            palabras = []
            for palabra in archivo:
                palabra = palabra.strip()
                palabras.append(palabra)
            
            palabraGenerada = random.choice(palabras)
        return palabraGenerada
    
    except Exception as e:
        print(f"Ocurrio un error: {e}")    
    

def generarArchivoDePalabras():
    palabras = [
    "perro", "gatos", "techo", "verde", "clave", "piano", "banco", "fuego", "calor", "doler",
    "comer", "lugar", "plaza", "torre", "puedo", "viene", "campo", "carta", "barco", "leche",
    "flota", "sello", "punto", "globo", "salta", "llama", "nieve", "truco", "silla", "plomo",
    "corto", "ancho", "besar", "rural", "noche", "rueda", "calle", "sueño", "dardo", "firma",
    "beber", "tonto", "crudo", "risas", "regla", "acero", "curso", "reloj", "golpe", "honor",
    "clase", "extra", "ramas", "temas", "juego", "signo", "tarea", "muero", "salir", "orden",
    "pilar", "venas", "joyas", "ritmo", "mundo", "grito", "zorro", "duros", "fotos", "vista",
    "letal", "vacas", "dices", "rojos", "lunes", "marco", "diario", "entra", "nunca", "falsa",
    "pobre", "votos", "cajas", "labio", "lento", "rayos", "girar", "grasa", "firme", "mayor",
    "naves", "joven", "lejos", "robar", "trajo", "rubio", "tocar", "tiene", "sacar", "suave",
    "coche", "tarta", "brisa", "niños", "frase", "huevo", "pisos", "bravo", "justo", "salud",
    "grave", "acaba", "pagar", "angel", "citas", "pista", "actos", "tumba", "trama", "canto",
    "fiesta", "abuso", "norma", "fruta", "ojala", "freno", "pacto", "ronda", "tinta", "votar",
    "siglo", "polvo", "avion", "ideas", "pasto", "hierro", "raton", "salto", "caida", "noble",
    "abajo", "tecla", "sabor", "motor", "picos", "botas", "lucir", "honra", "costo", "baile",
    "rayar", "harto", "mover", "dolor", "presa", "sigue", "asado", "gente", "pedir", "exito",
    "citar", "saben", "poeta", "huida", "llave", "carga", "corte", "ruina", "trago", "campe",
    "calza", "nacer", "plano", "tabla", "densa", "arbol", "santa", "cerca", "cazar", "limon",
    "aguas", "tenis", "humor", "jugar", "nadar", "reina", "moler", "pasos", "sabio", "piden",
    "hielo", "mojar", "trigo", "veloz", "nubes", "plena", "zarza", "tallo", "cerco", "cinta",
    "plato", "rodeo", "texto", "pulso", "finca", "tinto", "batir", "dados", "lapiz", "dones",
    "roble"
]
    
    rutaActual = os.path.dirname(__file__)
    rutaArchivo = os.path.join(rutaActual, "palabras.txt")
    
    try:
        with open(rutaArchivo, "w") as archivo:
            cantidad = random.randint(30, 100)
            seleccion = random.sample(palabras, cantidad)
            
            for palabra in seleccion:
                archivo.write(f"{palabra}\n")
        return "palabras.txt"
        
    except Exception as e:
        print(f"Ocurrio un error: {e}")       

def main():
    archivo = generarArchivoDePalabras()
    prepararPartida(archivo)
main()    