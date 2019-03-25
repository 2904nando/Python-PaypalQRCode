import requests
import json

invoiceID = "INV2-7JLK-XELW-LVTA-NYWJ"

url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/" + invoiceID

headers = {
    'Content-Type':'application/json',
    'Authorization':"Bearer A21AAHX3df5i-IjJPOMBehTujUNwjC2tEeHqkBWWg36AbW6FQUK727Djfe3bSxZYx28FU-zxLTfhP5cqVvQIReB2ljBSV55gw"
}

r = requests.get(url, headers=headers)
print(r.text)

paid = False

while paid == False:
    r = requests.get(url, headers=headers)
    response = json.loads(r.text)
    #print(r.text)
    if response['status'] == 'PAID':
        paid = True
    else:
        print('Unpaid')

if paid == True:
    #print(response)
    print('Invoice de R$'+ str(response['payments'][0]['amount']['value']) + " (de código " + invoiceID + ') foi pago com sucesso!')