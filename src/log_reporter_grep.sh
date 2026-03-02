#!/bin/bash

# ── 1. Recibir el nivel como argumento ──────────────────────────
NIVEL=$1

# Validar que se proporcionó un nivel
if [ -z "$NIVEL" ]; then
    echo "Uso: bash src/log_reporter_grep.sh [INFO|WARN|ERROR|DEBUG]"
    exit 1
fi

# Convertir a mayúsculas por si el usuario escribe minúsculas
NIVEL=$(echo "$NIVEL" | tr '[:lower:]' '[:upper:]')

# Validar que el nivel sea válido
if [[ "$NIVEL" != "INFO" && "$NIVEL" != "WARN" && "$NIVEL" != "ERROR" && "$NIVEL" != "DEBUG" ]]; then
    echo "Nivel inválido. Usa: INFO, WARN, ERROR o DEBUG"
    exit 1
fi

# ── 2. Definir rutas ─────────────────────────────────────────────
ARCHIVO="data/log_muestra_app.log"
NIVEL_LOWER=$(echo "$NIVEL" | tr '[:upper:]' '[:lower:]')
SALIDA="out/${NIVEL_LOWER}_validos.txt"
REPORTE="out/reporte_log.json"

# Crear carpeta out/ si no existe
mkdir -p out

# ── 3. Expresión regular para línea válida ───────────────────────
REGEX="^\[$NIVEL\] [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} .+"

# ── 4. Filtrar líneas válidas y guardarlas ───────────────────────
grep -E "$REGEX" "$ARCHIVO" > "$SALIDA"

# ── 5. Contar líneas ─────────────────────────────────────────────
# Total de líneas no vacías
TOTAL=$(grep -c "." "$ARCHIVO")

# Total de líneas válidas
VALIDAS=$(grep -c -E "$REGEX" "$ARCHIVO")

# Líneas sospechosas: contienen el nivel pero no cumplen el formato
SOSPECHOSAS=$(grep -i "\[$NIVEL\]" "$ARCHIVO" | grep -v -E "$REGEX" | wc -l)

# ── 6. Mostrar en pantalla ───────────────────────────────────────
echo "===== Reporte de logs: $NIVEL ====="
echo "Total de líneas no vacías : $TOTAL"
echo "Total de líneas válidas   : $VALIDAS"
echo "Total de líneas sospechosas: $SOSPECHOSAS"

# ── 7. Generar reporte JSON ──────────────────────────────────────
cat > "$REPORTE" << EOF
{
  "nivel": "$NIVEL",
  "total_lineas": $TOTAL,
  "lineas_validas": $VALIDAS,
  "lineas_sospechosas": $SOSPECHOSAS,
  "archivo_salida": "$SALIDA"
}
EOF

echo ""
echo "✅ Líneas válidas guardadas en: $SALIDA"
echo "✅ Reporte JSON guardado en   : $REPORTE"
