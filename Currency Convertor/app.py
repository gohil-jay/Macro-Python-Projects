//python program to convert currency of one type to the currency of another type
//import the modules required
from forex_python.converter import CurrencyRates
c = CurrencyRates()
//Enter the amount to be converted
amount = int(input("Enter the amount: "))
//from_currency is the currency which you have entered
from_currency = input("From : ").upper()
//to_currency is the currency which you have entered
to_currency = input("To : ").upper()
//converting the entered currency to the required currency
result = c.convert(from_currency, to_currency, amount)
//printing the required converted currency
print("\n")
print(from_currency, "to", to_currency, ": ", result)
