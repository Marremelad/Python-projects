def main():
    total = 0
    amount_due = 50
    print("Insert Coin")
    while total < 50:
        print("Amount Due:", amount_due)
        pay = int(input())
        if pay != 25 and pay != 10 and pay != 5:
            total = 0
        else:
            amount_due -= pay
            total += pay

    if total > 50:
        print("Change Owed:", (total - 50))
    else:
        print("Change Owed:", 0)
main()



  