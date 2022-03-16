from unittest import TestCase
from functions import convert_currency,get_currency_code,validate_inputs

class FunctionsTestCase(TestCase):
  """Testing app functions"""

  def  test_convert_currency(self):
    self.assertEquals(convert_currency("USD", "USD", 100),100)
    self.assertEquals(convert_currency("GBP", "GBP", 1000),1000)

  def  test_currency_code(self):
    self.assertEquals(get_currency_code("USD"),"$")
    self.assertEquals(get_currency_code("GBP"),"£")

  def  test_validate_inputs(self):
    self.assertEquals(validate_inputs("USD","GBP"),True)
    self.assertEquals(validate_inputs("USD","GBPP"),None)