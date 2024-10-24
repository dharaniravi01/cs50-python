def main():
    groceries = {}
    try:
        while True:
            grocery = input().upper()
            if grocery in groceries:
                groceries[grocery] += 1
            else:
                groceries[grocery] = 1
    except EOFError:
        print('')
        for grocery in sorted(groceries):
            print(f'{groceries[grocery]} {grocery}')




main()
