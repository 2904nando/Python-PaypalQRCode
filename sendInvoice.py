import requests

invoiceID = "INV2-7JLK-XELW-LVTA-NYWJ"

url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/" + invoiceID + "/send?notify_merchant=true"

headers = {
    'Content-Type':'application/json',
    'Authorization':"Bearer A21AAEd6rBLqKLNvGeib09EcRGRoDeXw60_kT7_yZ0NHq-M71ah_h0NHQYdtES_0F77AywKUc0VmqTLL4gav2kXIdnHH1dMqQ"
}

r = requests.post(url,headers=headers)

print(r)