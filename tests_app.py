from unittest import TestCase
from app import app

app.config["TESTING"] = True


class RoutesTestCase(TestCase):
    """Testing flask routes"""

    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Fx Rate Converter</h1>", html)

    def test_currency_conversion(self):
        with app.test_client() as client:
            data = {"convert-from": "USD", "convert-to": "USD", "amount": 100}
            resp = client.post("/convert", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertIn("The converted amount is $100", html)
            self.assertEqual(resp.status_code, 200)

            data = {"convert-from": "USDD", "convert-to": "USD", "amount": 100}
            resp = client.post("/convert", data=data, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertIn(
                "Please enter a valid 3 letter currency code. For example: JPY", html
            )
