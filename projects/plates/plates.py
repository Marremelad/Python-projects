import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    lgth = len(plate)

    for i in range(lgth):
        if plate[i] in string.punctuation:
            return False

    if lgth < 2 or lgth > 6:
        return False

    if plate[0].isnumeric():
        return False
    elif plate[0].isalpha():
        if plate[1].isnumeric():
            return False

    if plate[lgth - 1].isalpha():
        if plate[round(lgth / 2)].isnumeric():
            return False
        else:
            return True

    elif plate[round(lgth / 2)] == "0":
        return False
    else:
        return True
if __name__ == "__main__":
    main()

