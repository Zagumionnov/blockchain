"""a flask web interface for the blockchain"""

from flask import Flask, render_template, request, redirect, url_for

from block import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    """getting data from the form and pass
    it to the block creation function"""

    if request.method == 'POST':
        lender = request.form.get('lender')
        amount = request.form.get('amount')
        borrower = request.form.get('borrower')

        write_block(lender, amount, borrower)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route("/check", methods=['GET'])
def check():
    """Block integrity check"""

    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
