def main():
    deep(input("What is the universes ulitmate answer? ").lower().replace(" ", "").replace("-", ""))

def deep(text):
   match text:
        case "42" | "fortytwo":
            print("Yes")
        case _:
            print("No")
main()
