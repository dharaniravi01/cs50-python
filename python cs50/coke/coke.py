#show amt due and ask for coins
amt_due = 50
while True:
    print("Amount Due:", amt_due)
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
       amt_due -= insert
       if amt_due <= 0:
            print("Change Owed:", -amt_due)
            break


