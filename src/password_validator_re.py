import re
import sys
import os

# ── 1. Definir rutas ─────────────────────────────────────────────
ARCHIVO = "data/passwords_muestra.txt"
VALIDAS = "out/validas.txt"
INVALIDAS = "out/invalidas.txt"

# Crear carpeta out/ si no existe
os.makedirs("out", exist_ok=True)

# ── 2. Función principal de validación ──────────────────────────
def is_valid(password):
    razones = []

    # Regla 1: longitud >= 8
    if len(password) < 8:
        razones.append("longitud insuficiente")

    # Regla 2: al menos una mayúscula
    if not re.search(r'[A-Z]', password):
        razones.append("no tiene mayúscula")

    # Regla 3: al menos un dígito
    if not re.search(r'[0-9]', password):
        razones.append("no tiene dígito")

    # Regla 4: solo letras y números
    if re.search(r'[^a-zA-Z0-9]', password):
        razones.append("tiene caracteres inválidos")

    return len(razones) == 0, razones

# ── 3. Leer archivo y clasificar ────────────────────────────────
with open(ARCHIVO, "r", encoding="utf-8") as f:
    passwords = [l.strip() for l in f.readlines() if l.strip() != ""]

validas = []
invalidas = []
razones_conteo = {
    "longitud insuficiente": 0,
    "no tiene mayúscula": 0,
    "no tiene dígito": 0,
    "tien
