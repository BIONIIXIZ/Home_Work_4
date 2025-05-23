from pathlib import Path


def total_salary(path):
    try:
        Path(path).open(encoding="utf-8")
        file_path = Path(path)
        total_sum = 0
        count = 0
        users = ()
        with file_path.open(mode = "r", encoding="utf-8") as file:
            for line in file:
                contents = line.strip().split(',')
                try:
                    salary = float(contents[1])
                    total_sum += salary
                    count += 1
                except ValueError:
                    print(f"Помилка виникла в рядку: {line.strip()}")

            avarage = total_sum / count
            return (total_sum, avarage)
    except FileNotFoundError:
        print(f"path {file_path} is not Found.")
        return (0,0)