import inflect

p = inflect.engine()

def main():

    names =[]
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break
    changed = p.join(names)
    print("Adieu, adieu, to " + changed)




main()
