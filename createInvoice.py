import requests

url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/"

headers = {
    'Content-Type':'application/json',
    'Authorization':"Bearer A21AAEd6rBLqKLNvGeib09EcRGRoDeXw60_kT7_yZ0NHq-M71ah_h0NHQYdtES_0F77AywKUc0VmqTLL4gav2kXIdnHH1dMqQ"
}

data = """
{
"merchant_info": {
    "email":"nando-facilitator@kyan.com.br",
    "first_name":"Luis Fernando",
    "last_name":"Boschiero Kumruyan",
    "business_name":"Loja Teste",
    "phone": {
        "country_code":"055",
        "national_number":"123445678"
    }
},
"items": [{
    "name":"Sapato Masculino",
    "quantity":2,
    "unit_price": {
        "currency":"BRL",
        "value":59.99
    }},{
    "name":"Sandalia",
    "quantity":1,
    "unit_price": {
        "currency":"BRL",
        "value":35.99
    }
}],
"note": "Obrigado pela compra!",
"terms": "Devolucao ate 30 dias com nota fiscal"
}

"""

r = requests.post(url,headers=headers,data=data)

print(r.text)