import requests
import json

from flask import Flask

merchant = {'email': 'nando-facilitator@kyan.com.br', 'firstName': 'Luis Fernando', 'lastName': 'Boschiero Kumruyan', 'businessName': 'LojaTeste', 'phoneCountryCode': '055', 'phone': '12345678'}

produtos = [
    {'nome': 'Sapato Masculino', 'quantidade':2, 'preco': 59.99},
    {'nome': 'Sandalia', 'quantidade':3, 'preco': 19.99},
    {'nome': 'Tenis preto', 'quantidade':1, 'preco': 154.99},
    {'nome': 'Calca grande', 'quantidade':2, 'preco': 250.00},
    {'nome': 'Calca masculina', 'quantidade': 3, 'preco': 21.99}
]

nota = "Agradecemos pela sua compra!"

termos = "Devolucoes em ate 30 dias, mediante apresentacao da nota fiscal original"

headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer A21AAHX3df5i-IjJPOMBehTujUNwjC2tEeHqkBWWg36AbW6FQUK727Djfe3bSxZYx28FU-zxLTfhP5cqVvQIReB2ljBSV55gw"
    }

def createInvoice(listaProdutos, dictMerchant, notes, terms):

    #Adicionar infos do merchant

    strMerchant = '"merchant_info": {"email": "%s", "first_name": "%s", "last_name": "%s", "business_name": "%s", "phone": {"country_code": "%s", "national_number": "%s"}}' % (dictMerchant['email'], dictMerchant['firstName'],dictMerchant['lastName'],dictMerchant['businessName'],dictMerchant['phoneCountryCode'],dictMerchant['phone'])

    strProds = '"items": ['

    for produto in listaProdutos:
        pName = produto['nome']
        pQuant = produto['quantidade']
        pPreco = produto['preco']

        strProd = '{"name": "%s", "quantity": %d, "unit_price": {"currency": "BRL", "value": %.2f}}' % (pName,pQuant,pPreco)

        strProds += strProd + ", "

    strProds = strProds[:-2] + "]"

    strData = '{%s, %s, "note": "%s", "terms": "%s"}' % (strMerchant, strProds, notes, terms)

    #print(strData)

    url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/"

    r = json.loads(requests.post(url, headers=headers, data=strData).text)

    return r['id']

    #print(r)

def sendInvoice(invoiceID):

    url = 'https://api.sandbox.paypal.com/v1/invoicing/invoices/%s/send?notify_merchant=true' % invoiceID

    r = requests.post(url, headers=headers)

def createQRCode(invoiceID):

    url = 'https://api.sandbox.paypal.com/v1/invoicing/invoices/%s/qr-code' % invoiceID

    r = json.loads(requests.get(url, headers=headers).text)

    return r['image']

idInvoice = createInvoice(produtos,merchant,nota,termos)
sendInvoice(idInvoice)
imgB64 = createQRCode(idInvoice)

app = Flask(__name__)

@app.route('/')
def index():
    retorno = '<img src="data:image/png;base64, ' + imgB64 + '"/>'
    return retorno

if __name__ == "__main__":
    app.run(debug=True)