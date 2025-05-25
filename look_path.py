import sys
from colorama import Fore , Style, init
from pathlib import Path

init(autoreset=True)



def walking_on_dir(path: Path, indent: int = 0):
    for item in sorted(path.iterdir()):
        prefix = " " * (indent * 4)  # кожен рівень — це 4 пробіли

        if item.is_dir():
            print(f"{prefix}{Fore.LIGHTRED_EX}{item.name}/{Style.RESET_ALL}")
            walking_on_dir(item, indent + 1)
        else:
            print(f"{prefix}{Fore.LIGHTGREEN_EX}{item.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print("Write your path in terminal like this --> python(3) 'name.py' 'your path' ")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists() or not dir_path.is_dir():
        print("Current path is not correct or its not a directory.")
        sys.exit(1)

    print(f"{Fore.LIGHTBLUE_EX}{dir_path.name}/{Style.RESET_ALL}")
    walking_on_dir(dir_path, indent=1)

if __name__ == "__main__":
    main()










