import random

def main():
    #prompt for a level n

    while True:
        try:
            n = int(input("Level: "))
            if n <= 0:
                continue
            else:
                #random generate integer
                num = random.randint(1, n)
                #ask to guess
                guess = int(input("Guess: "))
                if guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too Large!")
                elif guess == num:
                    print("Just Right!")
                    break




        except ValueError:
            continue



main()
