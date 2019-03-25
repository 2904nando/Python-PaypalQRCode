import requests
import json

from flask import Flask

app = Flask(__name__)

invoiceID = "INV2-7JLK-XELW-LVTA-NYWJ"

url="https://api.sandbox.paypal.com/v1/invoicing/invoices/" + invoiceID + "/qr-code"

headers = {
    'Content-Type':'application/json',
    'Authorization':"Bearer A21AAEd6rBLqKLNvGeib09EcRGRoDeXw60_kT7_yZ0NHq-M71ah_h0NHQYdtES_0F77AywKUc0VmqTLL4gav2kXIdnHH1dMqQ"
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