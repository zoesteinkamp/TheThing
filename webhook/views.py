from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import json
import requests
from os.path import join, dirname
from watson_developer_cloud import DialogV1 as Dialog

@parser_classes((JSONParser,))
def btc(request, format=None):

    m = request.GET.get('message')

    msg = m.lower()

    if msg == "buy":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/buy?qty=1'
    elif msg == "sell":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/sell?qty=1'
    elif msg == "spot":
        url = 'https://montanaflynn-bitcoin-exchange-rate.p.mashape.com/prices/spot_rate?currency=USD'
    else:
        return HttpResponse("I don't understand")

    headers = {'X-Mashape-Key': 'KjbSKQZgASmsh8v3S9kuvoRJ5Hbrp1zaJDXjsniwy1J3Ooc7IA', 'Accept': 'text/plain'}
    r = requests.get(url, headers=headers)

    res = json.loads(r.content)

    if msg == "spot":
        ret = res[u'amount']
    else:
        ret = res[u'total'][u'amount']

    return HttpResponse(ret)




@parser_classes((JSONParser,))
def travel(request, format=None):

    msg = request.GET.get('message')

    print "endpoint hit, msg: " + msg

    if msg == 'Hello' or msg == 'Hi' or msg == 'Hi im travis' or msg == "hi" or msg == "hey":
        response = "Hi I'm Watson. Im here to help your family or buisness plan their vacation fast! Where would you like to go?"
    elif msg == 'I want to go to seattle' or msg == 'id like to go to seattle' or msg == 'Seattle' or msg == 'seattle':
        response = "I will gladly book you a trip for Seattle. Where are you flying from?"
    elif msg == 'Denver' or msg == 'from denver' or msg == 'denver':
        response = "What dates would you like to go?"
    elif msg == "I want to go March 13 to March 16" or msg == "March 13 to March 16" or msg == "march 13 to march 16":
        response = "Alright, what is your budget for round trip tickets?"
    elif msg == "500" or msg == "500 dollars":
        print "500!!!"
        response = "Alright I found these flights: A 233 round trip ticket on Alaska Airlines with no stops. A 337 round trip ticket on United with no stops."
    elif msg == "I want the first" or msg == "one" or msg == "First flight":
        response = "Fantastic! Lets get you a airbnb place as well! Would you like to have your own place or private room?"
    elif msg == "my own place" or msg == "My own" or msg == "private room":
        response = "Okay what is your budget a night for that private place?"
    elif msg == "200 a night" or msg == "200" or msg == "200 dollars":
        response = "Great, here are the top two rated airbnb private rentals: Vintage Downtown Seattle Studio and Highland Hideaway SpaceNeedle View."
    elif msg == "the first" or msg == "number one" or msg == "First place":
        response = "Do you want to save to Quickbooks?"
    # elif request.GET.get('message') == "I would":

    else:
        response = "Sorry, I don't understand."

    print "response: " + response

    return HttpResponse(response)


@parser_classes((JSONParser,))
def watson(request, format=None):

    dialog = Dialog(username='13323f71-1c0f-4279-97b2-642ad24969ae', password='f8GyTJ7LAB1b')

    response = (dialog.conversation("a1b083fe-4c88-4059-be93-8ec0258bba13")['response'])

    print response[0]

    return HttpResponse(response[0])


@parser_classes((JSONParser,))
def intuit(request, format=None):


    return HttpResponse("Quickbooks!")
