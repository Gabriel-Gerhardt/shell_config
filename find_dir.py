#!/usr/bin/env python3
import os
import sys

def find_dir(target_name):
    target_name_lower = target_name.lower()
    ignore_dirs = {'node_modules', '.git', '__pycache__'}  # pode adicionar mais aqui

    for root, dirs, files in os.walk('.'):
        # Remove os diretórios a serem ignorados para não descer neles
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        dirs_lower = [d.lower() for d in dirs]
        if target_name_lower in dirs_lower:
            index = dirs_lower.index(target_name_lower)
            path = os.path.join(root, dirs[index])
            print(path)
            return 0
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: find_dir.py <nome_diretorio>", file=sys.stderr)
        sys.exit(1)

    target = sys.argv[1]
    if find_dir(target) != 0:
        print(f"Diretório '{target}' não encontrado.", file=sys.stderr)
        sys.exit(1)
