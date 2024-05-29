import re
def main():

    month =  [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    while True:
        date = input("Date: ").strip()
        array = re.split("[/// " "]", date.lower().title().replace(",", "").replace('"', ""))

        if len(array) > 3:
            continue

        if array[0] in month:

            a = int(array[1])

            if "/" in date:
                continue

            elif "," not in date:
                continue

            elif a < 1 or a > 31:
                continue

            else:
                lgth = len(month)
                for i in range(lgth):
                    if array[0] == month[i]:
                        array[0] = f"{i + 1}"

                buffer = array[0]
                array[0] = array[1]
                array[1] = buffer

                lgth = len(array)

                print(array[2], end = "-")
                print(f"{int(array[1]):02}", end = "-")
                print(f"{int(array[0]):02}")
                break

        else:
            if array[0].isdigit():
                try:
                    a = int(array[0])
                    b = int(array[1])
                except ValueError:
                    continue

                if a < 1 or a > 12 or b < 1 or b > 31:
                    continue

                else:
                    buffer = array[0]
                    array[0] = array[1]
                    array[1] = buffer

                    lgth = len(array)

                    print(array[2], end = "-")
                    print(f"{int(array[1]):02}", end = "-")
                    print(f"{int(array[0]):02}")
                    break
            else:
                continue

main()

