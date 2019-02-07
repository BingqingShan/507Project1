from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the banking application!'

@app.route('/bank/<name>')
def bankname(name):
    one_bank= Bank(name).name
    return:'Welcome to'+ one_bank.__repr__()

@app.route('/dollar/<amt>')
def dollaramount(amt):
    dollar_amount= Dollar(int(amt))
    return: dollar_amount.__repr__()

@app.route('/yuan/<amt>')
def yuanamount(amt):
    yuan_amount= Yuan(int(amt))
    return: yuan_amount.__repr__()

@app.route('/pound/<amt>')
def poundamount(amt):
    pound_amount= Pound(int(amt))
    return: pound_amount.__repr__()

@app.route('/bank/<name>/<currency>/<value>')
def bankinfo(name,  currency, value):
    bank_info= Bank(name,  currency, int(value))
    return: 'Welcome to the NAME bank!'+bank_info.__repr__()
