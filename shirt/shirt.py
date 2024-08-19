import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input - Path")
        sys.exit(1)
    elif not format_check(sys.argv[1]) and format_check(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not format_same(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        fit_shirt(sys.argv[1], sys.argv[2])

def format_check(input_filetype):
    valid_formats = ["jpg", "jpeg", "png"]
    _, fn_ext = input_filetype.split(".", maxsplit=1)

    if fn_ext in valid_formats:
        return True
    else:
        return False

def format_same(input_file, output_file):
    _, fn_ext = input_file.split(".", maxsplit=1)

    if output_file.endswith(fn_ext):
        return True
    else:
        return False

def fit_shirt(input_file, output_file):
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))

    photo.paste(shirt, shirt)
    photo.save(output_file)

if __name__ == "__main__":
    main()
