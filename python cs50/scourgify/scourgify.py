import sys, csv

def main():
    #get two command line prompt
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        before_csv = sys.argv[1]
        after_csv = sys.argv[2]

        try:
            #open the csv
            with open(before_csv) as file:
                names = csv.DictReader(file)

                #get the fullnames into a list
                fullnames = []
                for name in names:
                    fullname = name["name"]

                    #separate the fullnames into two names
                    last, first = fullname.split(",")
                    first = first.strip()
                    last = last.strip()

                    #store first, last, house in fullnames
                    house = name["house"]
                    fullnames.append({"first": first, "last": last, "house": house})


            #write the new csv with updated names
            with open(after_csv, "w", newline = "") as file:
                write = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
                write.writeheader()
                write.writerows(fullnames)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a CSV file")


main()

