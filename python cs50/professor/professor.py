import random


def main():
     #ask for level btw 1-3
    level = get_level()

    #loop for 10 times
    score = 0
    times = 1
    while times < 11:
        #generate integer x and y
        x, y = generate_integer(level)
        attempts = 0
        #loop for 3 attemps
        while attempts < 3:
            ans = input(f"{x} + {y} = ")
            #exit loop when ans is correct

            if int(ans) == (x + y):
                times += 1
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {x + y}")
            times += 1

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
            else:
                continue
        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y





if __name__ == "__main__":
     main()
