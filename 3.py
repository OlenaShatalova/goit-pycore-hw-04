import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def show_directory_structure(path: Path, indent: int = 4):
    for item in sorted(path.iterdir()):
        if item.name == ".DS_Store":
            continue

        if item.is_dir():
            print(" " * indent + Fore.BLUE + f"{item.name}")
            show_directory_structure(item, indent + 4)

        else:
            print(" " * indent + Fore.GREEN + f"{item.name}")


if len(sys.argv) < 2:
    print("Please provide a directory path")
else:
    directory = Path(sys.argv[1])

    if not directory.exists():
        print("Path does not exist")

    elif not directory.is_dir():
        print("Path is not a directory")

    else:
        print(Fore.YELLOW + f"{directory.name}")
        show_directory_structure(directory)