#Sandbox account: nando-facilitator@kyan.com.br
#Client ID: ASNNEmRa17ShTMGbpU0BHGdGJij7OquQFyCTlnENr9C1XYilMojQfs69rKPkGpoTx40FveMlCZ4T9zgK
#Secret: EGJ6FKbmYOcyGdd46N76C0pTDO3On0TAIOytzI_1TMhQRjkiZTBMNpO6dFRRApc92GTF23djUaLXzxb_

import requests

url = "https://api.sandbox.paypal.com/v1/oauth2/token"

data = 'grant_type=client_credentials'

r = requests.post(url, data=data, auth=('ASNNEmRa17ShTMGbpU0BHGdGJij7OquQFyCTlnENr9C1XYilMojQfs69rKPkGpoTx40FveMlCZ4T9zgK','EGJ6FKbmYOcyGdd46N76C0pTDO3On0TAIOytzI_1TMhQRjkiZTBMNpO6dFRRApc92GTF23djUaLXzxb_'))

print(r.text)