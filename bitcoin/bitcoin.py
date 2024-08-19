import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            number = float(sys.argv[1])
            print(bitcoin_price(number))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def bitcoin_price(num):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None

if __name__ == "__main__":
    main()