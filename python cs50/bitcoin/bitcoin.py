import requests
import sys


def main():

    try:
        #exit if user never give anyth
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")

        #exit if user never give number
        elif not sys.argv[1].isdigit() and sys.argv[1].isdecimal():
            sys.exit("Command-line argument is not a number")

        else:
            api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            api_j = api.json()
            rate = api_j["bpi"]["USD"]["rate_float"]
            value = float(rate) * float(sys.argv[1])
            print(f"${value:,.4f}")


    except requests.RequestException:
        pass

main()





