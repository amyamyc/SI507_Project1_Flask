from flask import Flask
from lab3_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return 'Just the home page, nothing interesting.'

@app.route('/bank/<name>')
def see_new_bank_name(name):
    new_bank_name = Bank(name, Dollar, 0)
    return "Welcome to {}".format(new_bank_name.name)

@app.route('/dollar/<amt>')
def see_dollar(amt):
    new_dollar = Dollar(int(amt)) # creating an instance of class Dollar
    return new_dollar.__str__()

@app.route('/yuan/<amt>')
def see_yuan(amt):
    new_yuan = Yuan(int(amt)) #creating an instance of the class Yuan
    return new_yuan.__str__()

@app.route('/pound/<amt>')
def see_pound(amt):
    new_pound = Pound(int(amt))
    return new_pound.__str__()

@app.route('/bank/<name>/<currency>/<value>')
def message(name, currency, value):
    if currency == "Dollar":
        currency_class = Dollar
    elif currency == "Pound":
        currency_class = Pound
    elif currency == "Yuan":
        currency_class = Yuan
    else:
        return "Invalid URL inputs for bank"
# Have to call the Dollar class because Bank class requires an instance of the currency class
    x = Bank(name, currency_class, int(value))
    string = x.__str__()

    return "Welcome to the {} bank!".format(x.name) + string

if __name__ == "__main__":
    app.run()
