from django.shortcuts import render, HttpResponse
from . models import *

def vypis_temy(request):
    temy = Tema.objects.all().order_by("nazov")
    
    return HttpResponse(temy)

