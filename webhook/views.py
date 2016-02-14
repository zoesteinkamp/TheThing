from django.http import HttpResponse
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@parser_classes((JSONParser,))
def webhook(request, format=None):

    if request.method == "POST":
        data = JSONParser().parse(request)
        return HttpResponse(data["message"])