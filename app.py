from flask import Flask, request, render_template
from forms import validate_amount_type, validate_currency, calc_converted_currency

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret-key"

@app.route("/")
def index():
    """Shows home page with related forms"""
    return render_template("index.html")

@app.route('/form-check', methods =["POST"])
def form_inputs_validate():
    """Validates the inputs from the form and renders appropriate html template"""
    if request.method == "POST":
        
        currency_from = request.form["currency-from"]
        currency_to = request.form["currency-to"]
        amount = request.form["amount"]

        valid_currency_from = validate_currency(currency_from)
        valid_currency_to = validate_currency(currency_to)
        valid_amount_type = validate_amount_type(amount)
    
        ## initialize the err msgs to update later
        
        error_msgs = []

        if not valid_currency_from:
            err_currency_from = f"Invalid Country Code: {currency_from}"
            error_msgs.append({"id": "currency_from", "msg": err_currency_from})
        if not valid_currency_to:
            err_currency_to = f"Invalid Country Code: {currency_to}"
            error_msgs.append({"id": "currency_to", "msg": err_currency_to})
        if not valid_amount_type:
            err_amount = "Invalid Amount"
            error_msgs.append({"id": "amount", "msg": err_amount})

        converted_result = calc_converted_currency(currency_from,currency_to,amount)

        if error_msgs:
            return render_template("index.html", errors = error_msgs, conv_result = converted_result)
        else:
            return render_template("index.html", conv_result = converted_result)
    




