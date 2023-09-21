from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, static_url_path='/static')

expenses = []

@app.route('/')
def index():
    total = sum(expense['amount'] for expense in expenses)
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))

    if description and amount > 0:
        expenses.append({'description': description, 'amount': amount})

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

