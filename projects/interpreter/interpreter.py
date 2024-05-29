def main():
    calculation(expression = input("Expression ").split())

def calculation(expression):
    if expression[1] == "+":
        print(float(expression[0]) + float(expression[2]))

    elif expression[1] == "-":
        print(float(expression[0]) - float(expression[2]))

    elif expression[1] == "*":
        print(float(expression[0]) * float(expression[2]))

    elif expression[1] == "/":
        print(float(expression[0]) / float(expression[2]))

    else:
        print("Not a valid expression")
main()
