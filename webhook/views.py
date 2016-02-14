from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


@parser_classes((JSONParser,))
def webhook(request, format=None):

    if request.GET.get('message') == 'Hello' or 'Hi' or 'Hi im travis' or "hi" or "hey":
        response = "Hi I'm Watson. Im here to help your family or buisness plan their vacation fast! Where would you like to go?"
    elif request.GET.get('message') == 'I want to go to seattle' or 'id like to go to seattle' or 'Seattle' or 'seattle':
        response = "I will gladly book you a trip for Seattle. Where are you flying from?"
    elif request.GET.get('message') == 'Denver' or 'from denver' or 'denver':
        response = "What dates would you like to go?"
    elif request.GET.get('message') == "I want to go March 13 to March 16" or "March 13 to March 16" or "march 13 to march 16":
        response = "Alright, what is your budget for round trip tickets?"
    elif request.GET.get('message') == "500" or "500 dollars":
        response = " Alright I found these flights Which one would you like me to book?"
    elif request.GET.get('message') == "I want the first" or "one" or "first flight":
        response = "Fantastic! Lets get you a airbnb place as well! Would you like to have your own place or private room?"
    elif request.GET.get('message') == "my own place" or "my own" or "private room":
        response = "Okay what is your budget a night for that private place?"
    elif request.GET.get('message') == "200 a night" or "200" or "200 dollars":
        response = "Great, here are the top two rated airbnb private rentals in Seattle for 200 dollars a night for those dates. Please pick your prefered one. "
    elif request.GET.get('message') == "the first" or "number one" or "first place":
        response = "Alright I have your flight and place booked. Would you like some reservations for resturaunts in the area?"
    # else if request.GET.get('message') == "I would":

    else:
        response = "Sorry, I don't understand."
    return HttpResponse(response)
