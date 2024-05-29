def main():

    fraction = input("Fraction ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):

    x, y = fraction.split("/")

    if int(y) > 0 and int(x) > int(y):
        raise ValueError
    return round((int(x) / int(y)) * 100)

def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return F"{percentage}%"

if __name__ == "__main__":
    main()
