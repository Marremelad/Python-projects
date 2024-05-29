import validators

def main():

    print(validate(input("What is your email? ")))

def validate(email):

    if validators.email(email):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
