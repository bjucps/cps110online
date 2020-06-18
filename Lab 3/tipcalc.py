from flask import Flask, request

app = Flask(__name__)

def computeBill(billAmount: float) -> (float, float, float):
    tipAmount = billAmount * 0.15
    taxAmount = billAmount * 0.05
    totalAmount = billAmount + taxAmount + tipAmount

    return tipAmount, taxAmount, totalAmount    

@app.route('/')
def default():
    return """<html><body>
        <h2>Welcome to the tip calculator!</h2>
        I calculate tips for a restaurant bill. 
        You must supply input via an appropriately formed URL 
        with a query string. Can you figure out how to get me 
        to calculate a bill?
        </body>
        </html>
        """

@app.route('/calctip')
def calctip():
    billAmt = request.args.get('billAmt', '')
    if billAmt != '':
        billAmt = float(billAmt)

        tipAmt, taxAmt, totalAmt = computeBill(billAmt)

        return CALCTIP_HTML.format(billAmt, tipAmt, taxAmt, totalAmt)
    else:
        return """<html>You didn't supply a billAmt parameter.</html>"""


CALCTIP_HTML = """<html><body>
<h2>Joe's Restaurant</h2>
<h3>Bill of Sale</h3>
<table border='1'>
    <tr><td>Amount of Bill:</td><td>${0:.2f}</td></tr>
    <tr><td>Tip:</td><td>${1:.2f}</td></tr>
    <tr><td>Tax:</td><td>${2:.2f}</td></tr>
    <tr><td>Total:</td><td>${3:.2f}</td></tr>
</table>
</body></html>
"""

if __name__ == "__main__":
    # Launch the web server 
    app.run(host="localhost", debug=True)
    