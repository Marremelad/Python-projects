def main():
    str_time = input("What time is it? ").strip()

    float_time = convert(str_time)

    if 7.0 <= float_time <= 8.0:
        print("breakfast time")

    elif 12.0 <= float_time <= 13.0:
        print("lunch time")

    elif 18.0 <= float_time <= 19.0:
        print("dinner time")

    else:
        return

def convert(time):
    n = time.split(":")

    hrs = float(n[0])

    mins = float(n[1]) * 1 / 60

    return float(hrs + mins)

if __name__ == "__main__":
    main()
