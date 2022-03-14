from forex_python.converter import CurrencyRates, CurrencyCodes

currency_codes = CurrencyCodes()
currency_rates = CurrencyRates()

def convert_currency(from_fx,to_fx,amount):
  return currency_rates.convert(from_fx,to_fx,amount)

def get_currency_code(to_fx):
  return currency_codes.get_symbol(to_fx)