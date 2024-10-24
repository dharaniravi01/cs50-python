def main():

#ask for input
    reply = input()

    #convert the emojis qand print
    print(convert(reply))


def convert(reply):
   reply = reply.replace(':(','🙁').replace(':)','🙂')
   
   return reply


main()
