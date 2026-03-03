#regex-lag

Práctica de expresiones regulares aplicadas en Bash y Python.  
Materia: Teoría Matemática de la Computación  
Docente: Dr. José Luis Quiroz Fabián

---

# Estructura del repositorio

De acuerdo con los requerimientos obligatorios:
```
regex-lab/
├── README.md
├── data/
│   ├── log_muestra_app.log
│   └── passwords_muestra.txt
├── src/
│   ├── log_reporter_grep.sh
│   ├── log_reporter_re.py
│   ├── password_validator_grep.sh
│   └── password_validator_re.py
└── out/
```

---

#Requisitos

- Bash (Linux, macOS o WSL)
- Python 3.x (Módulo `re` incluido)

---

#Cómo ejecutar cada script

Importante: Todos los scripts deben ejecutarse desde la raíz del repositorio. La carpeta `out/` se generará automáticamente si no existe.

#1. Analizador de logs (Bash y Python)

Extraen líneas válidas y generan un reporte basado en el nivel especificado (INFO, WARN, ERROR, DEBUG).
```bash
bash src/log_reporter_grep.sh INFO
bash src/log_reporter_grep.sh ERROR
python3 src/log_reporter_re.py INFO
python3 src/log_reporter_re.py ERROR
```

**Salida:**
- `out/xxxx_validos.txt`: Líneas filtradas con formato correcto.
- `out/reporte_log.json`: Estadísticas del análisis en formato JSON.

---

#2. Validador de contraseñas (Bash y Python)

Clasifican las contraseñas del archivo de entrada según las reglas de seguridad definidas.
```bash
bash src/password_validator_grep.sh
python3 src/password_validator_re.py
```

**Salida:**
- `out/validas.txt`: Contraseñas que cumplen todos los criterios.
- `out/invalidas.txt`: Contraseñas rechazadas con su respectiva razón de rechazo.

---

#Reglas de validación aplicadas

# Logs de sistema
- Formato: `[NIVEL] AAAA-MM-DD HH:MM:SS Mensaje`
- Niveles: `INFO`, `WARN`, `ERROR`, `DEBUG`
- Mensaje: Debe contener al menos un carácter.

# Contraseñas
- Longitud mínima de 8 caracteres.
- Al menos una letra mayúscula.
- Al menos un dígito numérico.
- Restricción: Solo se permiten letras y números (alfanumérico).

---

# Reflexión final

**¿Por qué conviene validar datos tanto en frontend como en backend?**  
La validación en el frontend mejora la experiencia del usuario al dar feedback instantáneo y ahorra recursos al evitar peticiones innecesarias. Sin embargo, la validación en el backend es indispensable para la seguridad, ya que las capas de cliente pueden ser manipuladas o ignoradas por atacantes; el backend es el único que garantiza la integridad final de los datos almacenados.

**¿Qué limitaciones tienen las expresiones regulares en sistemas reales?**  
Las expresiones regulares están limitadas a lenguajes regulares dentro de la Jerarquía de Chomsky. No pueden procesar estructuras anidadas o recursivas (como HTML o JSON balanceado) ni validar lógica semántica avanzada, como comprobar si una fecha es válida cronológicamente (ej. evitar un 30 de febrero). Además, diseños ineficientes pueden causar problemas de rendimiento por retroceso catastrófico (backtracking).(backtracking).
