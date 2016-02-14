from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser


@parser_classes((JSONParser,))
def webhook(request, format=None):
    if request.GET.get('message') == 'Hello':
        response = "Hi I'm Watson"
    else:
        response = "Sorry, I don't understand."
    return HttpResponse(response)