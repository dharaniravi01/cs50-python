
def main():
     while True:
            try:
                    x, y = input("Fraction: ").split("/")
                    if int(y) < int(x):
                           continue
                    fraction = int(x) / int(y)
                    if convert(fraction) <= 1:
                        print("E")

                    elif convert(fraction) >= 99:
                        print("F")

                    else:
                        print(f"{convert(fraction)}%")
                    break
            except ValueError:
                   pass
            except ZeroDivisionError:
                   pass



def convert(s):
           percent = s * 100
           return round(percent)


main()
