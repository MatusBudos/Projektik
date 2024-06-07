from django.shortcuts import render, HttpResponse
from . models import *


def vypis_temy(request):
    temy = Tema.objects.all().order_by("dostupnost")
    return render(request, "soc/index.html", {"temy":temy})

def vypis_temu(request, tema):
    tema = Tema.objects.get(id = tema)
    return render(request, "soc/tema_detail.html", {"tema":tema})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(id = ucitel)
    temy = Tema.objects.filter(konzultant = ucitel)
    return render(request, "soc/ucitel_temy.html", {"ucitel":ucitel, "temy":temy})

def vypis_studenta(request, student):
    student = Student.objects.get(id = student)
    temy = Tema.objects.get(student = student)
    return render(request, "soc/ucitel_temy.html", {"student":student, "tema":temy})

def vypis_statistiku(request):
    pocet_tem = Tema.objects.count()
    pocet_obsadenych = Tema.objects.filter(dostupnost = 3).count()
    pocet_volnych = Tema.objects.filter(dostupnost = 1).count()
    pocet_cakajucich = Tema.objects.filter(dostupnost = 2).count()
    pocet_studentov = Student.objects.count()
    pocet_ucitelov = Ucitel.objects.count()
    return render(request, "soc/statistiky.html", {"temy":pocet_tem, "obsadene":pocet_obsadenych, "volne":pocet_volnych, "cakajuce":pocet_cakajucich, "studenti":pocet_studentov, "ucitelia": pocet_ucitelov})


