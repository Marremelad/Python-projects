def main():
    print(convert(text=input("Input string ")))

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()
