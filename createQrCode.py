import requests
import json

from flask import Flask

app = Flask(__name__)

invoiceID = "INV2-7JLK-XELW-LVTA-NYWJ"

url="https://api.sandbox.paypal.com/v1/invoicing/invoices/" + invoiceID + "/qr-code"

headers = {
    'Content-Type':'application/json',
    'Authorization':"*Auth*"
}

r = requests.get(url,headers=headers)
response = json.loads(r.text)

@app.route("/")
def qrCode():
    retorno = '<img src="data:image/png;base64, ' + response['image'] + '"/>'
    return retorno

#print(r.text)

if __name__ == "__main__":
    app.run(debug=True)