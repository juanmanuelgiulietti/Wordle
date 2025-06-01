# 🎮 Wordle en Python (Versión por Consola)

Este es un proyecto personal que recrea el clásico juego de Wordle, adaptado para ejecutarse en la terminal. El objetivo es adivinar una palabra secreta en una cantidad limitada de intentos, recibiendo pistas visuales por cada letra.

---

## 📌 Características

- ✅ Juego completamente funcional por consola.
- ✅ Lógica de juego fiel al Wordle original.
- ✅ Tres niveles de dificultad:
  - Fácil (5 letras, 7 intentos)
  - Medio (6 letras, 6 intentos)
  - Difícil (7 letras, 5 intentos)
- ✅ Validación de entrada del usuario.
- ✅ Verificación contra un diccionario de palabras.
- ✅ Registro de partidas (historial guardado en `.txt`).
- ✅ Uso de pistas tipo Wordle: 🟩 correcto, 🟨 está pero mal ubicada, ⬜ incorrecta.
- ✅ Múltiples partidas por sesión.

---

## 🧠 ¿Qué se aprende con este proyecto?

- Estructura de funciones y orden lógico
- Lectura y escritura de archivos (`.txt`, `.json`)
- Manejo de listas, strings y condicionales
- Generación de datos aleatorios
- Validaciones de entrada robustas
- Control de flujo (`while`, `break`, `continue`)
- Buenas prácticas de organización de código

---

## ⚙️ Requisitos

- Python 3.x
- Archivo `palabras_wordle.json` con las listas de palabras por longitud (debe estar en el mismo directorio)

---

## ▶️ Cómo jugar

1. Ejecutá el archivo principal:
   ```bash
   python wordle.py