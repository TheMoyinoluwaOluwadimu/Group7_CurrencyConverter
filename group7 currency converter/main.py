import tkinter as tk

# exchange rates as a dictionary
exchange_rates = {
    'USD': {'EUR': 0.92, 'JPY': 132.78, 'NGN': 464.50, 'PND': 0.80},
    'EUR': {'USD': 1.09, 'JPY': 144.34, 'NGN': 504.93, 'PND': 0.88},
    'JPY': {'USD': 0.0075, 'EUR': 0.0069, 'NGN': 3.50, 'PND': 0.0060},
    'NGN': {'USD': 0.0022, 'EUR': 0.0020, 'JPY': 0.29, 'PND': 0.0017},
    'PND': {'USD': 1.24, 'NGN': 569.62, "EUR": 1.14}
}

# Create the GUI window
root = tk.Tk()
root.title("Group Currency Converter")  # Sets title of the window
# Sizes the GUI window
root.geometry("450x400")
# sets background for the gui window
root.configure(bg="#00B2EE")


# Define function to convert currencies
def convert_currency():
    # Get the selected currencies and amount to convert
    from_currency = menu.get()
    to_currency = menu2.get()
    amount = float(amount_entry.get())

    # Convert the currency using the exchange rates from the dictionary
    converted_amount = amount * exchange_rates[from_currency][to_currency]

    # Display the converted amount in the result
    result_label.config(text=f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


# label for enter amount
amount_label = tk.Label(root, text="Enter amount:")
# configuring the foreground, background color and font family and size
amount_label.configure(fg="white", bg="#00B2EE", font=("Arial", 17, "bold"))
amount_label.pack(pady=10)

# entry / input box for amount
amount_entry = tk.Entry(root, width=20, font=("Arial", 12))
amount_entry.pack()

from_currency_label = tk.Label(root, text="Convert from:")
# configuring the foreground, background color and font family and size
from_currency_label.configure(fg="white", bg="#00B2EE", font=("Arial", 16, "bold"))
from_currency_label.pack(pady=10)

#setting
menu = tk.StringVar(root)
menu.set("Select Currency")
from_currency_DropDown = tk.OptionMenu(root, menu, *exchange_rates.keys())
from_currency_DropDown.configure(bg="white", borderwidth=0)
from_currency_DropDown.pack()

to_currency_label = tk.Label(root, text="Convert to:")
to_currency_label.configure(fg="white", bg="#00B2EE", font=("Arial", 16, "bold"))
to_currency_label.pack(pady=10)

menu2 = tk.StringVar(root)
menu2.set("Select Currency")
to_currency_DropDown = tk.OptionMenu(root, menu2, *exchange_rates.keys())
to_currency_DropDown.configure(bg="white", borderwidth=0)
to_currency_DropDown.pack()

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.configure(fg="black", bg="white", font=("Arial", 16))
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.configure(fg="black", font=("consolas", 16))
result_label.pack(pady=10)

root.mainloop()
