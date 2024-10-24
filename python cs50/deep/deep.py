qn = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

if qn.lower() == "forty two" or "forty-two":
    print('Yes')
elif qn.lower().strip() == "42":
    print("yes")
else:
    print('No')

