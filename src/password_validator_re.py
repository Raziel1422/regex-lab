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

    if len(password) < 8:
        razones.append("longitud insuficiente")

    if not re.search(r'[A-Z]', password):
        razones.append("no tiene mayúscula")

    if not re.search(r'[0-9]', password):
        razones.append("no tiene dígito")

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
    "tiene caracteres inválidos": 0
}

for password in passwords:
    valida, razones = is_valid(password)
    if valida:
        validas.append(password)
    else:
        invalidas.append(password)
        for razon in razones:
            razones_conteo[razon] += 1

# ── 4. Guardar resultados ────────────────────────────────────────
with open(VALIDAS, "w", encoding="utf-8") as f:
    f.write("\n".join(validas))

with open(INVALIDAS, "w", encoding="utf-8") as f:
    f.write("\n".join(invalidas))

# ── 5. Mostrar resultados ────────────────────────────────────────
print("===== Validador de contraseñas =====")
print(f"Total válidas  : {len(validas)}")
print(f"Total inválidas: {len(invalidas)}")
print("")
print("-- Razones de rechazo --")
for razon, conteo in razones_conteo.items():
    print(f"{razon:30}: {conteo}")
print("")
print(f"✅ Válidas guardadas en  : {VALIDAS}")
print(f"✅ Inválidas guardadas en: {INVALIDAS}")
