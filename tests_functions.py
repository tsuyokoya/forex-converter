from unittest import TestCase
from functions import convert_currency, get_currency_code, validate_inputs


class FunctionsTestCase(TestCase):
    """Testing app functions"""

    def test_convert_currency(self):
        self.assertEqual(convert_currency("USD", "USD", 100), 100)
        self.assertEqual(convert_currency("GBP", "GBP", 1000), 1000)

    def test_currency_code(self):
        self.assertEqual(get_currency_code("USD"), "$")
        self.assertEqual(get_currency_code("GBP"), "£")
        self.assertIsNone(get_currency_code("GBPP"))
        self.assertIsNone(get_currency_code("asdf"))

    def test_validate_inputs(self):
        self.assertTrue(validate_inputs("USD", "GBP"))
        self.assertIsNone(validate_inputs("USD", "GBPP"))
        self.assertIsNone(validate_inputs("USDD", "GBP"))
