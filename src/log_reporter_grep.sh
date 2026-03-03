#!/bin/bash

# Validar entrada
if [ -z "$1" ]; then
    echo "Uso: $0 [INFO|WARN|ERROR|DEBUG]"
    exit 1
fi

NIVEL=$(echo "$1" | tr '[:lower:]' '[:upper:]')
FILE="data/log_muestra_app.log"
OUT_DIR="out"
mkdir -p "$OUT_DIR"

# Definición de Regex para formato válido
REGEX="^\[(INFO|WARN|ERROR|DEBUG)\] [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} .+"

# Cálculos
TOTAL_LINEAS=$(grep -c -v '^$' "$FILE")
LINEAS_VALIDAS_TOTAL=$(grep -E -c "$REGEX" "$FILE")
VALIDAS_NIVEL=$(grep -E "$REGEX" "$FILE" | grep -c "\[$NIVEL\]")

# Líneas sospechosas: contienen el nivel pero no cumplen el formato completo
SOSPECHOSAS=$(grep "\[$NIVEL\]" "$FILE" | grep -E -v -c "$REGEX")

# Guardar logs válidos del nivel especificado
grep -E "$REGEX" "$FILE" | grep "\[$NIVEL\]" > "$OUT_DIR/${NIVEL,,}_validos.txt"

# Mostrar resultados en pantalla
echo "Total de líneas no vacías: $TOTAL_LINEAS"
echo "Total de líneas válidas: $LINEAS_VALIDAS_TOTAL"
echo "Total de líneas sospechosas para $NIVEL: $SOSPECHOSAS"

# Generar JSON básico
cat <<EOF > "$OUT_DIR/reporte_log.json"
{
  "busqueda": "$NIVEL",
  "total_no_vacias": $TOTAL_LINEAS,
  "total_validas": $LINEAS_VALIDAS_TOTAL,
  "sospechosas": $SOSPECHOSAS
}
EOF
