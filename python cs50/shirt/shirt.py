import sys, os
from PIL import Image
from PIL import ImageOps

def main():
    #get two command line prompt and check for extension
    if len(sys.argv) == 3 and sys.argv[1].endswith(("jpg", "jpeg", "png")) and sys.argv[2].endswith(("jpg", "jpeg", "png")):

        try:
            #check whether extensions are same
            name1, ext1 = os.path.splitext(sys.argv[1])
            name2, ext2 = os.path.splitext(sys.argv[2])

            if ext1 == ext2:

                #open the shirt and input
                shirt = Image.open("shirt.png")
                photo = Image.open(sys.argv[1])

                #resize the input
                resize = ImageOps.fit(photo, shirt.size)

                #overlay shirt.png to top
                resize.paste(shirt, shirt)

                #save the overlay
                resize.save(sys.argv[2])

            else:
                sys.exit("Input and Output have different extensions")

        except FileNotFoundError:
            sys.exit("file not found")

    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Invalid Input")


main()
