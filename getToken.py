import requests

url = "https://api.sandbox.paypal.com/v1/oauth2/token"

data = 'grant_type=client_credentials'

r = requests.post(url, data=data, auth=('*ClientID*','*Secret*'))

print(r.text)