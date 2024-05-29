import sys
import requests

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    rate = response.json()["bpi"]["USD"]["rate_float"]

    print(response)
    print(f"${rate * float(sys.argv[1]):,.4f}")

main()
