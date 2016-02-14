from django.http import HttpResponse

def webhook(request):
    return HttpResponse("Hai!")
