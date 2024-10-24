#ask for input
def main():
    answer = input("camelCase: ")
    convert(answer)

def convert(s):
    names =""
    for cap in s:
        if cap.isupper():
            names +=  "_" + cap.lower()
        else:
            names += cap
    print("snake_case: " + names)
    
main()

















