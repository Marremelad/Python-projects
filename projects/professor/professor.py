import random

def main():

    level = get_level()

    points = 0
    for _ in range(10):

            x = generate_integer(level)
            y = generate_integer(level)

            while True:
                print(f"{x} + {y} =", end = "")
                try:
                    answer = int(input(" "))
                    break
                except ValueError:
                    pass

            if answer == x + y:
                points += 1

            else:
                print("EEE")

                for i in range(2):

                    while True:
                        print(f"{x} + {y} =", end = "")
                        try:
                            answer = int(input(" "))
                            break
                        except ValueError:
                            pass

                    if answer == x + y:
                        points += 1
                        break

                    elif i == 1:
                        print(f"{x} + {y} = {x + y}")
                        break

                    else:
                        print("EEE")

    print(f"Score: {points}")


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                continue
            else:
                return level
        except ValueError:
            pass

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10,99)

    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
