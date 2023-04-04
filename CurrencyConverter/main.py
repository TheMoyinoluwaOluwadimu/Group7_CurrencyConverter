# Dictionary for the exchange rates
exchange_rates = {
    'USD': {'EUR': 0.92, 'JPY': 132.78, 'NGN': 464.50},
    'EUR': {'USD': 1.09, 'JPY': 144.34, 'NGN': 504.93},
    'JPY': {'USD': 0.0075, 'EUR': 0.0069, 'NGN': 3.50},
    'NGN': {'USD': 0.0022, 'EUR': 0.0020, 'JPY': 0.29}
}


# Function to convert currency
def currency_converter(amount, from_currency, to_currency):
    converted_amount = amount * exchange_rates[from_currency][to_currency]
    return converted_amount


# A while loop to convert the currencies and reiterate after usage
while True:
    print("***********CURRENCY CONVERTER***********")
    print("Welcome")
    amount = float(input("Enter amount You want to convert: "))
    from_currency = input("Enter the currency you want to convert from (USD, EUR, JPY, NGN): ")
    to_currency = input("Enter the currency you want to convert to (USD, EUR, JPY, NGN): ")

    converted_amount = currency_converter(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

    currency_converter(amount, from_currency, to_currency)
    answer = input("Do you want to convert another currency? (Y/N): ").upper()
    if answer != "Y":
        break
