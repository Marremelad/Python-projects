import inflect

def main():

    p = inflect.engine()
    array = []

    while True:
        try:
            array += [input("Name ").strip().title()]
        except EOFError:
            print()
            print("Adieu, adieu, to", p.join(array))
            break
main()
