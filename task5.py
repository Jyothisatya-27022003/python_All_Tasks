# Task 5: Currency Converter

import requests

def get_exchange_rate(base_currency, target_currency):
    try:
        # Free API for currency conversion (use your API key if required)
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad response

        data = response.json()

        # Check if target currency exists in response
        if target_currency.upper() not in data["rates"]:
            print("⚠️ Invalid target currency code.")
            return None

        # Return the exchange rate
        return data["rates"][target_currency.upper()]

    except requests.exceptions.RequestException as e:
        print(f"❌ Network or API error: {e}")
        return None
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        return None


def currency_converter():
    print("💱 Welcome to the Real-Time Currency Converter!")
    print("Example currency codes: USD, INR, EUR, GBP, JPY, AUD, etc..\n")

    base_currency = input("Enter the base currency (From): ").upper()
    target_currency = input("Enter the target currency (To): ").upper()

    try:
        amount = float(input(f"Enter amount in {base_currency}: "))
        if amount <= 0:
            print("⚠️ Amount must be greater than zero.")
            return
    except ValueError:
        print("⚠️ Invalid amount! Please enter a numeric value.")
        return

    print("\nFetching real-time exchange rate...")

    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        print(f"\n✅ {amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        print("❌ Conversion failed. Please check your inputs or try again later.")


# --- Main Program ---
if __name__ == "__main__":
    currency_converter()
