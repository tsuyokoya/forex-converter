from flask import Flask, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from functions import convert_currency, get_currency_code

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# session['converted_amount'] = ''
# session['converted_amount_symbol'] = ''


@app.route('/')
def show_home_page():
  """Returns home page"""
  return render_template('index.html')

@app.route('/convert',methods=['POST'])
def get_currency_data():
  """Converts amount to correct currency amount"""
  from_fx = request.form["convert-from"]
  to_fx = request.form["convert-to"]
  amount = request.form["amount"]
  print(from_fx,to_fx,amount)

  result_amount = convert_currency(from_fx,to_fx,amount)
  result_symbol = get_currency_code(to_fx)

  session['converted_amount'] = result_amount
  session['converted_amount_symbol'] = result_symbol
  return redirect('/result')

@app.route('/result')
def show_result():
  """Returns converted currency amount"""
  return render_template('result.html')