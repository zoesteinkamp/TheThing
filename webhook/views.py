from django.http import HttpResponse

def webhook(request):
    return HttpResponse("re: " + request.data.message)
