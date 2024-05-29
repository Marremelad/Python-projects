import re

def main():

    print(convert(input("Hours: ")))

def convert(s):

    regex = "([1-9]|1[0-2]):?([0-5][\\d])? (AM|PM)"
    if match := re.search(r"^" + regex + " to " + regex + "$", s):
        start = format(match.group(1), match.group(2), match.group(3))
        end = format(match.group(4), match.group(5), match.group(6))
    else:
        raise ValueError

    return f"{start} to {end}"

def format(hours, minutes, suffix):

    if hours == "12" and suffix == "AM":
        hours = "00"

    if suffix == "AM":
        hours = f"{int(hours):02}"
    elif suffix == "PM" and hours != "12":
        hours = f"{int(hours) + 12}"

    if minutes == None:
        minutes = "00"

    return f"{hours}:{minutes}"

if __name__ == "__main__":
    main()
