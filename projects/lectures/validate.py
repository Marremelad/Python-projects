import re

def main():
    ip = input("ip ")
    if re.search(ip_adress(), ip):
        print("Hello")

def ip_adress():

    ip = "^((25[0-5]|2[0-4][0-9]|[0|1]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[0|1]?[0-9]?[0-9])$"
    return ip

main()
