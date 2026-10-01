import sys
import os
from datetime import datetime


dirs = []
filename = None
i = 1  # começa em 1 (índice 0 é o nome do script)
while i < len(sys.argv):
    if sys.argv[i] == "-d":
        i += 1
        while i < len(sys.argv) and sys.argv[i] != "-f":
            dirs.append(sys.argv[i])
            i += 1
    elif sys.argv[i] == "-f":
        i += 1
        if i < len(sys.argv):
            filename = sys.argv[i]
            i += 1

if not filename:
    print("Error: -f flag is required")
    sys.exit(1)

caminho_completo = os.path.join(*dirs) if dirs else "."
os.makedirs(caminho_completo, exist_ok=True)

lines = []
while True:
    content = input("Enter content line: ")
    if content == "stop":
        break
    lines.append(content)

if caminho_completo and caminho_completo != ".":
    file_path = os.path.join(caminho_completo, filename)
else:
    file_path = filename

with open(file_path, "a") as file:
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        file.write("\n")

    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, line in enumerate(lines, 1):
        file.write(f"{i} {line}\n")
