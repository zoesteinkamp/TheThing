from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@parser_classes((JSONParser,))
def webhook(request, format=None):

    return HttpResponse(request.GET.get('message'))