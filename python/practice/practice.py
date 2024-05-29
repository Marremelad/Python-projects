import inflect
def main():
    names = ["Mauricio", "Marre", "MC"]

    print(f"{inflect.engine.join(names)} likes this")

main()
