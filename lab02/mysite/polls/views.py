from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Nhan! You are at the polls index")
