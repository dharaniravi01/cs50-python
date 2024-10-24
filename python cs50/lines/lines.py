import sys


def main():
#make sure to get correct input .py
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        file_name = sys.argv[1]


        try:
            #open the python file and remove comments and whitespace
            with open(file_name, 'r') as file:
                codes = file.readlines()

                only_codes = []
                for code in codes:
                    stripped = code.lstrip()
                    if stripped.startswith("#") or stripped == "":
                        continue
                    else:
                        only_codes.append(stripped)
                print(len(only_codes))


        except FileNotFoundError:
            sys.exit("File does not exist")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Not a Python file")



main()
