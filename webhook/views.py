from django.http import HttpResponse
from rest_framework.decorators import parser_classes

@parser_classes((JSONParser,))
def webhook(request, format=None):
    return HttpResponse(request.data['message'])