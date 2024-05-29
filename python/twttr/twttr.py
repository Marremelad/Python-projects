def main():

    word = input("Word ")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_word = ""

    for char in word:
        if char.lower() in vowels:
            pass
        else:
            new_word += char

    return new_word
if __name__ == "__main__":
    main()
