def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = ".?!,;:-_'"
    if len(s) < 2:
        return False
    if not s[0].casefold() in alphabet:
        return False
    if not s[1].casefold() in alphabet:
        return False
    if not 6 >= len(s) >= 2:
        return False
    for letter in s:
        if letter in punctuation:
            return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False
        if s[i] == '0' and s[i - 2].isalpha():
            return False

    return True










main()
