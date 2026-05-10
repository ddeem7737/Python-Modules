import sys
from typing import IO


def main():
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
        return

    name = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accesing file '{name}'")

    try:
        file: IO = open(name, "r")
        print("---\n")

        content = file.read()

        print(content, end="")

        print("---")

        file.close()

        print(f"File '{name}' closed")

    except Exception as e:
        print(f"Error opening file '{name}': {e}")


main()
