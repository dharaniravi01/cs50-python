def main():
    tweet = input("Input: ")
    print("Output: ", shorten(tweet))

def shorten(word):
    new_tweet = ""
    for letter in word:
        match letter.casefold():
            case 'a'| 'e' | 'i' | 'o' | 'u':
                continue
            case _:
                new_tweet += letter
    return new_tweet






if __name__ == "__main__":
    main()
