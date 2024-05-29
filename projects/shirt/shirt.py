from PIL import Image, ImageOps
import os
import sys

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    extensions = [".jpg", ".jpeg", ".png"]
    extargv1 = os.path.splitext(sys.argv[1].lower())
    extargv2 = os.path.splitext(sys.argv[2].lower())

    if extargv1[1] not in extensions or extargv2[1] not in extensions:
        sys.exit("Invalid output")
    elif extargv1[1] != extargv2[1]:
        sys.exit("Input and output have different extensions")

    try:
        user_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    user_image = ImageOps.fit(user_image, shirt.size)
    user_image.paste(shirt,shirt)
    user_image.save(sys.argv[2])

main()
