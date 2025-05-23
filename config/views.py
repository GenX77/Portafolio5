# config/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Funciona la vista principal!")
