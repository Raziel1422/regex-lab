#!/bin/bash

FILE="data/passwords_muestra.txt"
OUT_DIR="out"
mkdir -p "$OUT_DIR"

VALID_FILE="$OUT_DIR/validas.txt"
INVALID_FILE="$OUT_DIR/invalidas.txt"

> "$VALID_FILE"
> "$INVALID_FILE"

V_COUNT=0
I_COUNT=0

while IFS= read -r pass || [ -n "$pass" ]; do
    REASONS=""
    
    # 1. Longitud >= 8
    if [[ ! ${#pass} -ge 8 ]]; then REASONS+="[longitud insuficiente] "; fi
    
    # 2. Al menos una mayúscula
    if [[ ! "$pass" =~ [A-Z] ]]; then REASONS+="[no tiene mayúscula] "; fi
    
    # 3. Al menos un dígito
    if [[ ! "$pass" =~ [0-9] ]]; then REASONS+="[no tiene dígito] "; fi
    
    # 4. Solo letras y números (sin caracteres especiales)
    if [[ "$pass" =~ [^a-zA-Z0-9] ]]; then REASONS+="[tiene caracteres inválidos] "; fi

    if [ -z "$REASONS" ]; then
        echo "$pass" >> "$VALID_FILE"
        ((V_COUNT++))
    else
        echo "$pass -> Razones: $REASONS" >> "$INVALID_FILE"
        echo "Password: $pass RECHAZADA por: $REASONS"
        ((I_COUNT++))
    fi
done < "$FILE"

echo "------------------------"
echo "Total Válidas: $V_COUNT"
echo "Total Inválidas: $I_COUNT"
