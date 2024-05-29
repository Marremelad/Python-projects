from tabulate import tabulate
import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    print(convert(sys.argv[1]))

def convert(file):

    row = []
    try:
        with open(file) as menu:
            for line in menu:
                row.append(line.strip().split(","))
    except FileNotFoundError:
        sys.exit("File does not exist")

    return tabulate(row, headers = "firstrow", tablefmt = "grid")

if __name__ == "__main__":
    main()
