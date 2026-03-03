import re
import os
import sys
import json

def process_logs(level_to_find):
    level_to_find = level_to_find.upper()
    input_path = "data/log_muestra_app.log"
    out_dir = "out"
    os.makedirs(out_dir, exist_ok=True)
    
    # Regex: [NIVEL] AAAA-MM-DD HH:MM:SS Mensaje
    regex_pattern = r'^\[(INFO|WARN|ERROR|DEBUG)\] \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} .+'
    
    total_non_empty = 0
    total_valid = 0
    suspicious = 0
    valid_lines_content = []

    if not os.path.exists(input_path):
        print(f"Error: No se encuentra {input_path}")
        return

    with open(input_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            total_non_empty += 1
            
            is_valid_format = re.match(regex_pattern, line)
            
            if is_valid_format:
                total_valid += 1
                if f"[{level_to_find}]" in line:
                    valid_lines_content.append(line)
            else:
                if f"[{level_to_find}]" in line:
                    suspicious += 1

    # Guardar resultados
    with open(f"{out_dir}/{level_to_find.lower()}_validos.txt", "w") as f:
        f.write("\n".join(valid_lines_content))

    report = {
        "busqueda": level_to_find,
        "total_no_vacias": total_non_empty,
        "total_validas": total_valid,
        "sospechosas": suspicious
    }

    with open(f"{out_dir}/reporte_log.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"Total de líneas no vacías: {total_non_empty}")
    print(f"Total de líneas válidas: {total_valid}")
    print(f"Total de líneas sospechosas para {level_to_find}: {suspicious}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 log_reporter_re.py [NIVEL]")
    else:
        process_logs(sys.argv[1])
