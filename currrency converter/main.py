import tkinter as tk

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

# Tkinter GUI window
root = tk.Tk()
root.title("Currency Converter")

# Labels
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="Converted Amount:").grid(row=4, column=0, padx=5, pady=5)

# Entry boxes
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)
from_currency_entry = tk.Entry(root)
from_currency_entry.grid(row=1, column=1, padx=5, pady=5)
to_currency_entry = tk.Entry(root)
to_currency_entry.grid(row=2, column=1, padx=5, pady=5)
converted_amount_label = tk.Label(root, text="")
converted_amount_label.grid(row=4, column=1, padx=5, pady=5)

# Function to handle the currency conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    converted_amount = currency_converter(amount, from_currency, to_currency)
    converted_amount_label.config(text=f"{converted_amount:.2f}")

# Button to convert the currency
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=1, padx=5, pady=5)

# Run the main loop
root.mainloop()
