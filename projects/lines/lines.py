import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    print(line_count(sys.argv[1]))

def line_count(file):

    total = 0
    try:
        with open(file) as file:
            for line in file:
                if line.isspace() or line.lstrip().startswith("#"):
                    continue
                else:
                    total += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return total

if __name__ == "__main__":
    main()
