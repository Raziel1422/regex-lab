# regex-lab

Práctica de expresiones regulares aplicadas en Bash y Python.  
Materia: Teoría Matemática de la Computación

---

## Estructura del repositorio
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

## Requisitos

- Bash (Linux/Mac o WSL en Windows)
- Python 3.x

---

## Cómo ejecutar cada script

> ⚠️ Todos los scripts deben ejecutarse desde la **raíz** del repositorio.

### 1. Analizador de logs — Bash
```bash
bash src/log_reporter_grep.sh INFO
bash src/log_reporter_grep.sh WARN
bash src/log_reporter_grep.sh ERROR
bash src/log_reporter_grep.sh DEBUG
```

**Salida:**
- `out/info_validos.txt` (o warn, error, debug según el nivel)
- `out/reporte_log.json`

---

### 2. Analizador de logs — Python
```bash
python src/log_reporter_re.py INFO
python src/log_reporter_re.py ERROR
```

**Salida:**
- `out/info_validos.txt` (o warn, error, debug según el nivel)
- `out/reporte_log.json`

---

### 3. Validador de contraseñas — Bash
```bash
bash src/password_validator_grep.sh
```

**Salida:**
- `out/validas.txt`
- `out/invalidas.txt`

---

### 4. Validador de contraseñas — Python
```bash
python src/password_validator_re.py
```

**Salida:**
- `out/validas.txt`
- `out/invalidas.txt`

---

## Reglas de validación

### Logs
Una línea es válida si cumple el formato:
```
[NIVEL] AAAA-MM-DD HH:MM:SS Mensaje
```
Donde NIVEL puede ser: `INFO`, `WARN`, `ERROR` o `DEBUG`

### Contraseñas
Una contraseña es válida si:
- Tiene 8 o más caracteres
- Contiene al menos una letra mayúscula
- Contiene al menos un dígito
- Solo contiene letras y números

---

## Reflexión final

**¿Por qué conviene validar datos tanto en frontend como en backend?**  
Validar solo en frontend es inseguro porque cualquier usuario puede saltarse esas validaciones manipulando el código del navegador. El backend es la última línea de defensa y garantiza que los datos sean correctos sin importar cómo llegaron.

**¿Qué limitaciones tienen las expresiones regulares en sistemas reales?**  
Las expresiones regulares no pueden validar contexto ni semántica. Por ejemplo, pueden verificar que una fecha tenga el formato correcto pero no que sea una fecha real (como 30 de febrero). Además, regex muy complejas son difíciles de mantener y pueden tener problemas de rendimiento con textos muy largos.

---
