import requests

invoiceID = "INV2-7JLK-XELW-LVTA-NYWJ"

url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/" + invoiceID + "/send?notify_merchant=true"

headers = {
    'Content-Type':'application/json',
    'Authorization':"*Auth*"
}

r = requests.post(url,headers=headers)

print(r)