from pathlib import Path

def get_cats_info(path):
    try:
        file_path = Path(__file__).parent / path
        cats = []
        with file_path.open(encoding="utf-8") as file:
            for line in file:
                part = line.strip().split(",")
                if len(part) == 3:
                    id = part[0]
                    name = part[1]
                    try:
                        age = int(part[2])
                        cats.append({"id": id, "name": name, "age": age})
                    except ValueError:
                        print(f"Некоректо введений вік:{part[2]}")

            return cats
    except FileNotFoundError:
        print(f"path {file_path} is not Found.")
        return []

