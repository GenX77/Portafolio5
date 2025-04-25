# escribe en un archivo estructura.txt la estructura de carpetas y archivos del proyecto
# para ejecutar --->> Python arbol.py

import os
import sys

def print_tree(startpath, prefix='', output=sys.stdout):
    for item in sorted(os.listdir(startpath)):
        path = os.path.join(startpath, item)
        if os.path.isdir(path) and item not in ['__pycache__', '.git', '.venv']:
            print(f"{prefix}├── {item}/", file=output)
            print_tree(path, prefix + "│   ", output)
        elif os.path.isfile(path):
            print(f"{prefix}├── {item}", file=output)

# Verifica si el archivo 'estructura.txt' existe, y si no, lo crea
output_file = "estructura.txt"

if not os.path.exists(output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        print_tree('.', output=f)
    print(f"Archivo '{output_file}' creado con éxito.")
else:
    print(f"El archivo '{output_file}' ya existe.")