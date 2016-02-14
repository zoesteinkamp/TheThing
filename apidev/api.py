import requests
import json

def webhook(req):

    msg = req.lower()

    if msg == "buy":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/buy?qty=1'
    elif msg == "sell":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/sell?qty=1'
    elif msg == "spot":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/spot_rate?currency=USD'
    else:
        return "I don't understand"

    headers = {'X-Mashape-Key': 'KjbSKQZgASmsh8v3S9kuvoRJ5Hbrp1zaJDXjsniwy1J3Ooc7IA', 'Accept': 'text/plain'}
    r = requests.get(url, headers=headers)

    res = json.loads(r.content)

    if msg == "spot":
        return res[u'amount']
    else:
        return res[u'total'][u'amount']

x = webhook("spot")
print x