import requests

url = "https://api.sandbox.paypal.com/v1/invoicing/invoices/"

headers = {
    'Content-Type':'application/json',
    'Authorization':"*Auth*"
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