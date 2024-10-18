# Simple Currency Converter

def currency_converter():
    # Define conversion rates (example rates)
    rates = {
        'USD_TO_EUR': 0.85,  # Example: 1 USD = 0.85 EUR
        'EUR_TO_USD': 1.18,  # Example: 1 EUR = 1.18 USD
        'USD_TO_INR': 74.50, # Example: 1 USD = 74.50 INR
        'INR_TO_USD': 0.013, # Example: 1 INR = 0.013 USD
        'EUR_TO_INR': 88.00, # Example: 1 EUR = 88.00 INR
        'INR_TO_EUR': 0.011, # Example: 1 INR = 0.011 EUR
    }

    print("Simple Currency Converter")
    print("1. USD to EUR")
    print("2. EUR to USD")
    print("3. USD to INR")
    print("4. INR to USD")
    print("5. EUR to INR")
    print("6. INR to EUR")

    choice = int(input("Enter your choice (1-6): "))
    amount = float(input("Enter the amount to convert: "))

    if choice == 1:
        converted = amount * rates['USD_TO_EUR']
        print(f"${amount} USD is €{converted:.2f} EUR")
    elif choice == 2:
        converted = amount * rates['EUR_TO_USD']
        print(f"€{amount} EUR is ${converted:.2f} USD")
    elif choice == 3:
        converted = amount * rates['USD_TO_INR']
        print(f"${amount} USD is ₹{converted:.2f} INR")
    elif choice == 4:
        converted = amount * rates['INR_TO_USD']
        print(f"₹{amount} INR is ${converted:.2f} USD")
    elif choice == 5:
        converted = amount * rates['EUR_TO_INR']
        print(f"€{amount} EUR is ₹{converted:.2f} INR")
    elif choice == 6:
        converted = amount * rates['INR_TO_EUR']
        print(f"₹{amount} INR is €{converted:.2f} EUR")
    else:
        print("Invalid choice!")

currency_converter()
