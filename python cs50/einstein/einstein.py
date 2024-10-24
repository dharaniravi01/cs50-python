

def main():
    #ask for mass
    m = int(input('m: '))
    print ('E: ', eqn(m))

def eqn(m):
    return m * pow(300000000, 2)

main()
