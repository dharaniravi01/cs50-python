def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    cost = []
    while True:
        try:
            item = input("Item: ").title()
            cost.append(menu.get(item))
            total = sum(cost)
            print(f'${total:.2f}')
            continue

        except EOFError:
            print('')
            break
        except TypeError:
            pass
        except KeyError:
            pass
















main()
