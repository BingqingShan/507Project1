from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the banking application!'

@app.route('/bank/<name>')
def bankname(name):
    bank_name= Bank(name,Dollar)
    return 'Welcome to '+ bank_name.name +'!'

@app.route('/dollar/<amt>')
def dollaramount(amt):
    dollar_amount= Dollar(int(amt))
    return dollar_amount.__str__()

@app.route('/pound/<amt>')
def poundamount(amt):
    pound_amount= Pound(int(amt))
    return pound_amount.__str__()

@app.route('/yuan/<amt>')
def yuanamount(amt):
    yuan_amount= Yuan(int(amt))
    return yuan_amount.__str__()

@app.route('/bank/<name>/<currency>/<value>')
def bankinfo(name,currency,value):
    if currency =="Dollar":
        bank_info=Bank(name,Dollar,int(value))
        return 'Welcome to the '+bank_info.name+' bank! '+bank_info.__str__()
    elif currency =="Pound":
        bank_info=Bank(name,Pound,int(value))
        return 'Welcome to the '+bank_info.name+' bank! '+bank_info.__str__()
    elif currency =="Yuan":
        bank_info=Bank(name,Yuan,int(value))
        return 'Welcome to the '+bank_info.name+' bank! '+bank_info.__str__()
    else:
        return 'Invalid URL inputs for bank.'

if __name__ == "__main__":
        app.run()
