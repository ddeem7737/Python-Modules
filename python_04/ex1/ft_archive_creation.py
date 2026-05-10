import sys
from typing import IO


def transform(content: str) -> str:
    transformed = ""
    for i in content:
        if i == "\n":
            transformed += "#\n"
        else:
            transformed += i
    return transformed


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

        print("Transformed data")
        print("---")

        new_content = transform(content)

        print(new_content, end="")

        save = input("Enter new file name (or empty): ")

        if save == "":
            print("No saving data.")
            return

        print(f"Saving data to '{save}'")

        save_file: IO = open(save, "w")
        save_file.write(new_content)
        save_file.close()

        print(f"Data saved in file '{save}'")

    except Exception as e:
        print(f"Error opening file '{name}': {e}")


main()
