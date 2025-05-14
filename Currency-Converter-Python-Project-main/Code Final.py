import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"

    def get_supported_currencies(self):
        return ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "JPY", "CNY", "SAR", "KWD"]

    def convert_currency(self, from_currency, to_currency, amount):
        try:
            response = requests.get(f"{self.api_url}{from_currency}")
            data = response.json()
            rate = data["rates"].get(to_currency, None)

            if rate:
                converted_value = float(amount) * rate
                return converted_value
            else:
                return None

        except Exception as e:
            raise e

if __name__ == "__main__":
    converter = CurrencyConverter()

    print("OUTPUT:-")
    from_curr = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_curr = input("Enter the currency to convert to (e.g., EUR): ").upper()
    amount_str = input("Enter the amount to convert: ")
    supported_currencies = converter.get_supported_currencies()
    if from_curr not in supported_currencies or to_curr not in supported_currencies:
        print("Error: Invalid currency selection.")
    else:
        try:
            amount = float(amount_str)
            converted_amount = converter.convert_currency(from_curr, to_curr, amount)

            if converted_amount is not None:
                print(f"{amount:.2f} {from_curr} is equal to {converted_amount:.2f} {to_curr}")
            else:
                print("Error: Conversion failed.")
        except ValueError:
            print("Error: Invalid amount entered.")
        except Exception as e:
            print(f"An error occurred during conversion: {e}")
