from unittest import TestCase
from app import app
from flask import session

app.config['TESTING'] = True

class RoutesTestCase(TestCase):
  """Testing flask routes"""

  def  test_home_page(self):
    with app.test_client() as client:
      res = client.get('/')
      self.assertEqual(res.status_code, 200)

  def test_redirection(self):
      with app.test_client() as client:
        resp = client.post('/convert')
        self.assertEqual(resp.status_code, 302)

  def test_redirection_followed(self):
      with app.test_client() as client:
        res = client.get('/result',follow_redirects=True)
        self.assertEqual(res.status_code, 200)