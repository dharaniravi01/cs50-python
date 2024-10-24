import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(sys.argv) == 3 and sys.argv[1] == "-f": #check for correct number and -f
        new_font = sys.argv[2] #assign font to 3rd position
        try:
            figlet.setFont(font = new_font)
        except:
            sys.exit("ERROR: provide font") #if no font was given then exit
    else:
        sys.exit("Type in \"python file.py -f fontname\" format") #if no -f and font given then exit

    #ask for input when the numbers are correct
    user = input("Input: ")
    print(figlet.renderText(user))


main()
