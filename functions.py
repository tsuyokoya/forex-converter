from forex_python.converter import CurrencyRates, CurrencyCodes

currency_codes = CurrencyCodes()
currency_rates = CurrencyRates()

def convert_currency(from_fx,to_fx,amount):
  """Convert currency to specified to_fx currency"""
  result_amount = currency_rates.convert(from_fx,to_fx,float(amount))
  return round(result_amount, 2)

def get_currency_code(to_fx):
  """Return currency symbol of specified to_fx currency"""
  return currency_codes.get_symbol(to_fx)

def validate_inputs(from_fx,to_fx):
  """Validate currency name, type as string, and length of 3"""
  validate_from_fx = currency_codes.get_symbol(from_fx) and isinstance(from_fx,str) and len(from_fx) == 3
  validate_to_fx = currency_codes.get_symbol(to_fx) and isinstance(to_fx,str) and len(to_fx) == 3
  return validate_from_fx and validate_to_fx