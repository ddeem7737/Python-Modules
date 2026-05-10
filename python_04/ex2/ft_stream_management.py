import sys
from typing import IO


def transform_data(content: str) -> str:
    transformed = ""

    for c in content:
        if c == '\n':
            transformed += "#\n"
        else:
            transformed += c

    if len(content) > 0 and content[-1] != '\n':
        transformed += "#"

    return transformed


def get_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()

    text = sys.stdin.readline()

    if len(text) > 0 and text[-1] == '\n':
        text = text[:-1]

    return text


def main():

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    name = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{name}'")

    try:
        file: IO = open(name, "r")

        print("---")

        content = file.read()

        print(content, end="")

        print("---")

        file.close()

        print(f"File '{name}' closed.")

        print("Transform data:")
        print("---")

        new_content = transform_data(content)

        print(new_content, end="")

        print("---")

        save = get_input("Enter new file name (or empty): ")

        if save == "":
            print("Not saving data.")
            return

        print(f"Saving data to '{save}'")

        try:
            save_file: IO = open(save, "w")

            save_file.write(new_content)

            save_file.close()

            print(f"Data saved in file '{save}'.")

        except Exception as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{save}': {e}\n"
            )

    except Exception as e:
        sys.stderr.write(
            f"[STDERR] Error opening file '{name}': {e}\n"
        )


main()
