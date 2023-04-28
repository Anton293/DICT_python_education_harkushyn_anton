import requests
import json


def send_request(currency_code):
    """request type 'get'"""
    try: 
        result = requests.get(f"https://www.floatrates.com/daily/{currency_code}.json")
        data_json = json.loads(result.text)
        return data_json
    
    except json.JSONDecodeError:
        print("Error currency code(invalid json)")
        return -1


def main():
    """head function"""
    while True:
        currency_code = input("Enter currency code: ").lower()
        if currency_code == "usd" or currency_code == "eur":
            print("'eur' or 'usd' -> error")
            continue
        data_json = send_request(currency_code)
        if data_json != -1:
            break
    
    cash = {"usd": data_json['usd'], "eur": data_json['eur']}
        
    while True:
        print(f'{"="*10}{currency_code.upper()}{"="*10}')
        input_currency = input("Currency: ").lower()
        try:
            input_user_amount = int(input("Enter amount: "))
        except ValueError:
            print("error input amount")

        if len(input_currency) != 3:
            print("error input currency")
            continue

        result = 0

        print("Checking the cache...")
        if input_currency in cash:
            print("It is in the cache!")
            result = round(input_user_amount*float(cash[input_currency]['rate']), 2)
        else:
            try:
                data_json = send_request(currency_code)
                cash[input_currency] = data_json[input_currency]
                result = round(input_user_amount*float(cash[input_currency]['rate']), 2)
            except ValueError:
                print("error")
                continue
        
        print(f"You received {result} {input_currency.upper()}.")


if __name__ == "__main__":
    main()
