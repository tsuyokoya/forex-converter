from flask import Flask, render_template, request, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from functions import convert_currency, get_currency_code, validate_inputs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

@app.route('/')
def show_home_page():
  """Returns home page"""
  return render_template('index.html')

@app.route('/convert',methods=['POST'])
def get_currency_data():
  """Stores result currency amount and gets currency symbol"""
  from_fx = request.form.get("convert-from")
  to_fx = request.form.get("convert-to")
  amount = request.form.get("amount")

  are_proper_fx_names = validate_inputs(from_fx,to_fx)

  if not are_proper_fx_names:
    flash('Please enter a valid 3 letter currency code. For example: JPY','error')
    return redirect('/')
  else:
    result_amount = convert_currency(from_fx,to_fx,amount)
    result_symbol = get_currency_code(to_fx)

    session['converted_amount'] = result_amount
    session['converted_amount_symbol'] = result_symbol
    return redirect('/result')

@app.route('/result')
def show_result():
  """Returns converted currency amount"""
  return render_template('result.html')