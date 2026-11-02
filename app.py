# TAX BRACKETS:
# $0 - $12,000 | 10%
# $12,001 - $50,000 | 15%
# Over $50,000 | 20%

from flask import Flask, request, render_template, redirect, url_for
from markupsafe import Markup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    income_text = request.form.get("income", "")
    if income_text == "":
        return "ERROR: Income field is required.", 400
    new_income = float(income_text)

    if new_income == 0:
        tax = 0
    elif new_income <= 12000:
        tax = new_income * 0.10
    elif new_income <= 50000:
        tax = (12000 * 0.10) + ((new_income - 12000) * 0.15)
    else:
        tax = (12000 * 0.10) + (38000 * 0.15) + ((new_income - 50000) * 0.20)
    if new_income < 0:
        return "ERROR: Income cannot be negative.", 400
    elif new_income == 0:
        return render_template('result.html', income=f"${new_income:.2f}", tax=f"$0.00")
    else:
        return render_template('result.html', income=f"${new_income:.2f}", tax=f"${tax:.2f}")

if __name__ == '__main__':
    app.run(debug=True)