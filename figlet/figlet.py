from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        sys.exit("Invalid usage")

    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        chosen_font = sys.argv[2]
        if chosen_font not in fonts:
            sys.exit("Invalid font")
        str_input = input("Input: ")
        figlet.setFont(font=chosen_font)
        print("Output: ")
        print(figlet.renderText(str_input))

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
