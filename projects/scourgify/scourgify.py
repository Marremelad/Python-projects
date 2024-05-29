import sys
import csv

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    clean(sys.argv[1], sys.argv[2])

def clean(input, output):

    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, "w") as output:
                writer = csv.DictWriter(output, fieldnames = ["first", "last", "house"])
                writer.writeheader()
                for line in reader:
                    last, first = line["name"].split(", ")
                    house = line["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

main()
