import re
import sys
import os

# ── 1. Recibir el nivel como argumento ──────────────────────────
if len(sys.argv) < 2:
    print("Uso: python src/log_reporter_re.py [INFO|WARN|ERROR|DEBUG]")
    sys.exit(1)

NIVEL = sys.argv[1].upper()

# Validar que el nivel sea válido
niveles_validos = ["INFO", "WARN", "ERROR", "DEBUG"]
if NIVEL not in niveles_validos:
    print("Nivel inválido. Usa: INFO, WARN, ERROR o DEBUG")
    sys.exit(1)

# ── 2. Definir rutas ─────────────────────────────────────────────
ARCHIVO = "data/log_muestra_app.log"
NIVEL_LOWER = NIVEL.lower()
SALIDA = f"out/{NIVEL_LOWER}_validos.txt"
REPORTE = "out/reporte_log.json"

# Crear carpeta out/ si no existe
os.makedirs("out", exist_ok=True)

# ── 3. Expresión regular para línea válida ───────────────────────
REGEX = rf"^\[{NIVEL}\] \d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}} .+"

# ── 4. Leer el archivo ───────────────────────────────────────────
with open(ARCHIVO, "r", encoding="utf-8") as f:
    lineas = f.readlines()

# ── 5. Clasificar líneas ─────────────────────────────────────────
lineas_no_vacias = [l for l in lineas if l.strip() != ""]
lineas_validas = [l for l in lineas if re.match(REGEX, l.strip())]
lineas_sospechosas = [
    l for l in lineas
    if re.search(rf"\[{NIVEL}\]", l, re.IGNORECASE)
    and not re.match(REGEX, l.strip())
]

# ── 6. Guardar líneas válidas ────────────────────────────────────
with open(SALIDA, "w", encoding="utf-8") as f:
    f.writelines(lineas_validas)

# ── 7. Mostrar en pantalla ───────────────────────────────────────
print(f"===== Reporte de logs: {NIVEL} =====")
print(f"Total de líneas no vacías  : {len(lineas_no_vacias)}")
print(f"Total de líneas válidas    : {len(lineas_validas)}")
print(f"Total de líneas sospechosas: {len(lineas_sospechosas)}")

# ── 8. Generar reporte JSON ──────────────────────────────────────
reporte = f"""{{
  "nivel": "{NIVEL}",
  "total_lineas": {len(lineas_no_vacias)},
  "lineas_validas": {len(lineas_validas)},
  "lineas_sospechosas": {len(lineas_sospechosas)},
  "archivo_salida": "{SALIDA}"
}}"""

with open(REPORTE, "w", encoding="utf-8") as f:
    f.write(reporte)

print(f"\n✅ Líneas válidas guardadas en: {SALIDA}")
print(f"✅ Reporte JSON guardado en   : {REPORTE}")
