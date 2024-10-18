import streamlit as st

# Define conversion rates (example rates)
rates = {
    'USD_TO_EUR': 0.85,  # Example: 1 USD = 0.85 EUR
    'EUR_TO_USD': 1.18,  # Example: 1 EUR = 1.18 USD
    'USD_TO_INR': 74.50, # Example: 1 USD = 74.50 INR
    'INR_TO_USD': 0.013, # Example: 1 INR = 0.013 USD
    'EUR_TO_INR': 88.00, # Example: 1 EUR = 88.00 INR
    'INR_TO_EUR': 0.011, # Example: 1 INR = 0.011 EUR
}

# Streamlit app layout
st.title("Simple Currency Converter")

# Dropdown to select conversion option
conversion_option = st.selectbox(
    "Choose the conversion:",
    (
        "USD to EUR",
        "EUR to USD",
        "USD to INR",
        "INR to USD",
        "EUR to INR",
        "INR to EUR"
    )
)

# Input amount to convert
amount = st.number_input("Enter the amount to convert:", min_value=0.0, format="%.2f")

# Perform conversion based on the user selection
if st.button("Convert"):
    if conversion_option == "USD to EUR":
        converted_amount = amount * rates['USD_TO_EUR']
        st.write(f"${amount} USD is €{converted_amount:.2f} EUR")
    elif conversion_option == "EUR to USD":
        converted_amount = amount * rates['EUR_TO_USD']
        st.write(f"€{amount} EUR is ${converted_amount:.2f} USD")
    elif conversion_option == "USD to INR":
        converted_amount = amount * rates['USD_TO_INR']
        st.write(f"${amount} USD is ₹{converted_amount:.2f} INR")
    elif conversion_option == "INR to USD":
        converted_amount = amount * rates['INR_TO_USD']
        st.write(f"₹{amount} INR is ${converted_amount:.2f} USD")
    elif conversion_option == "EUR to INR":
        converted_amount = amount * rates['EUR_TO_INR']
        st.write(f"€{amount} EUR is ₹{converted_amount:.2f} INR")
    elif conversion_option == "INR to EUR":
        converted_amount = amount * rates['INR_TO_EUR']
        st.write(f"₹{amount} INR is €{converted_amount:.2f} EUR")
