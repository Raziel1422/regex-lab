#!/bin/bash

# ── 1. Definir rutas ─────────────────────────────────────────────
ARCHIVO="data/passwords_muestra.txt"
VALIDAS="out/validas.txt"
INVALIDAS="out/invalidas.txt"

# Crear carpeta out/ si no existe
mkdir -p out

# Limpiar archivos de salida anteriores
> "$VALIDAS"
> "$INVALIDAS"

# ── 2. Contadores ────────────────────────────────────────────────
total_validas=0
total_invalidas=0
razon_longitud=0
razon_mayuscula=0
razon_digito=0
razon_caracteres=0

# ── 3. Procesar cada contraseña ──────────────────────────────────
while IFS= read -r password || [ -n "$password" ]; do

    # Ignorar líneas vacías
    [ -z "$password" ] && continue

    es_valida=true

    # Regla 1: longitud >= 8
    if [ ${#password} -lt 8 ]; then
        es_valida=false
        razon_longitud=$((razon_longitud + 1))
    fi

    # Regla 2: al menos una mayúscula
    if ! echo "$password" | grep -q '[A-Z]'; then
        es_valida=false
        razon_mayuscula=$((razon_mayuscula + 1))
    fi

    # Regla 3: al menos un dígito
    if ! echo "$password" | grep -q '[0-9]'; then
        es_valida=false
        razon_digito=$((razon_digito + 1))
    fi

    # Regla 4: solo letras y números
    if echo "$password" | grep -q '[^a-zA-Z0-9]'; then
        es_valida=false
        razon_caracteres=$((razon_caracteres + 1))
    fi

    # ── 4. Guardar en el archivo correspondiente ─────────────────
    if [ "$es_valida" = true ]; then
        echo "$password" >> "$VALIDAS"
        total_validas=$((total_validas + 1))
    else
        echo "$password" >> "$INVALIDAS"
        total_invalidas=$((total_invalidas + 1))
    fi

done < "$ARCHIVO"

# ── 5. Mostrar resultados ────────────────────────────────────────
echo "===== Validador de contraseñas ====="
echo "Total válidas  : $total_validas"
echo "Total inválidas: $total_invalidas"
echo ""
echo "-- Razones de rechazo --"
echo "Longitud insuficiente   : $razon_longitud"
echo "Sin mayúscula           : $razon_mayuscula"
echo "Sin dígito              : $razon_digito"
echo "Caracteres inválidos    : $razon_caracteres"
echo ""
echo "✅ Válidas guardadas en  : $VALIDAS"
echo "✅ Inválidas guardadas en: $INVALIDAS"
