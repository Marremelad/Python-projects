def main():

    groceries = {}

    while True:
        try:
            item = input().upper().strip()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            break

    new_groceries = dict(sorted(groceries.items()))

    for key in new_groceries:
        print(f"{new_groceries[key]} {key}")

main()
