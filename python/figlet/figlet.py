import sys
import random
from pyfiglet import Figlet

def main():

    figlet = Figlet()
    arg_array = ["-f", "--font"]
    font_array = figlet.getFonts()

    if len(sys.argv) == 1:
        figlet.setFont(font = random.choice(font_array))

    elif len(sys.argv) == 3:
        if not sys.argv[1] in arg_array or not sys.argv[2] in font_array:
            sys.exit("Invalid usage")
        else:
            figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")

    print(figlet.renderText(input("Text: ")))

main()

