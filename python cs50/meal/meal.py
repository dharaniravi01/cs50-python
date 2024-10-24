#ask for time
def main():
    time = input("What time is it? ")

    x = convert(time)
    if 7 <= x <= 8:
        print("breakfast time")

    if 12 <= x <= 13:
        print("lunch time")

    if 18 <= x <= 19:
        print("dinner time")



def convert(time):
    h, m = time.split(":")
    return float(h) + float(m) / 60


if __name__ == "__main__":
    main()
