import re
import os

def is_valid(password):
    reasons = []
    if len(password) < 8:
        reasons.append("longitud insuficiente")
    if not re.search(r'[A-Z]', password):
        reasons.append("no tiene mayúscula")
    if not re.search(r'\d', password):
        reasons.append("no tiene dígito")
    if re.search(r'[^a-zA-Z0-9]', password):
        reasons.append("tiene caracteres inválidos")
    
    return len(reasons) == 0, reasons

def main():
    input_path = "data/passwords_muestra.txt"
    out_dir = "out"
    os.makedirs(out_dir, exist_ok=True)
    
    valid_list = []
    invalid_list = []

    if not os.path.exists(input_path):
        return

    with open(input_path, 'r') as f:
        passwords = f.read().splitlines()

    for p in passwords:
        valid, reasons = is_valid(p)
        if valid:
            valid_list.append(p)
        else:
            invalid_list.append(f"{p} (Razones: {', '.join(reasons)})")
            print(f"Password: {p} RECHAZADA: {reasons}")

    with open(f"{out_dir}/validas.txt", "w") as f:
        f.write("\n".join(valid_list))
    
    with open(f"{out_dir}/invalidas.txt", "w") as f:
        f.write("\n".join(invalid_list))

    print(f"\nTotal Válidas: {len(valid_list)}")
    print(f"Total Inválidas: {len(invalid_list)}")

if __name__ == "__main__":
    main()
