import sys
import os

def start():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        print(line_counter(sys.argv[1]))


def line_counter(script_file):
    skipped_lines = 0

    with open(script_file, "r") as file_lines:

        all_lines = list(enumerate(file_lines.readlines(), start=1))

        for line_num, content in all_lines:
            if (
                content.strip().startswith("#")
                or content.strip().startswith("\n")
                or content.isspace()
            ):
                skipped_lines += 1

    return int(all_lines[-1][0]) - skipped_lines

if __name__ == "__main__":
    start()
