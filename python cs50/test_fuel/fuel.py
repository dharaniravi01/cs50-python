
def main():
    while True:
        fraction = input("Fraction: ")
        print(gauge(convert(fraction)))
        break
        


def convert(s):
    try:
        x, y = s.split("/")
        if int(x) > int(y):
            raise ValueError
        percent = (int(x) / int(y)) * 100
        return round(percent)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


def gauge(s):
    if s <= 1:
        return "E"
    elif s >= 99:
        return "F"
    else:
        return f"{s}%"




if __name__ == "__main__":
    main()
