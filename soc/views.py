from django.shortcuts import render, HttpResponse
from . models import *


def vypis_temy(request):
    temy = Tema.objects.all().order_by("dostupnost")
    konzultanti = Ucitel.objects.filter()
    odbory = Odbor.objects.all()
    dostupnost = Dostupnost.objects.all()
    return render(request, "soc/index.html", {"temy":temy, "konzultanti":konzultanti, "odbory":odbory, "dostupnost":dostupnost})

def vypis_temu(request, tema):
    tema = Tema.objects.get(id = tema)
    return render(request, "soc/tema_detail.html", {"tema":tema})

def vypis_ucitela(request, ucitel):
    ucitel = Ucitel.objects.get(id = ucitel)
    temy = Tema.objects.filter(konzultant = ucitel)
    return render(request, "soc/ucitel_temy.html", {"ucitel":ucitel, "temy":temy})

def vypis_studenta(request, student):
    student = Student.objects.get(id = student)
    temy = Tema.objects.filter(student = student)
    return render(request, "soc/ucitel_temy.html", {"student":student, "tema":temy})

def vypis_statistiku(request):
    pocet_tem = Tema.objects.count()
    pocet_obsadenych = Tema.objects.filter(dostupnost = 3).count()
    pocet_volnych = Tema.objects.filter(dostupnost = 1).count()
    pocet_cakajucich = Tema.objects.filter(dostupnost = 2).count()
    pocet_studentov = Student.objects.count()
    pocet_ucitelov = Ucitel.objects.count()
    return render(request, "soc/statistiky.html", {"temy":pocet_tem, "obsadene":pocet_obsadenych, "volne":pocet_volnych, "cakajuce":pocet_cakajucich, "studenti":pocet_studentov, "ucitelia": pocet_ucitelov})

from django.shortcuts import render, redirect
from .models import Tema

def nova_tema(request):
    if request.method == 'GET':
        konzultant = Ucitel.objects.all()
        student = Student.objects.all()
        odbor = Odbor.objects.all()
        dostupnost = Dostupnost.objects.all()
        return render(request, "soc/nova_tema.html", {"konzultant":konzultant, "student":student, "odbor":odbor, "dostupnost":dostupnost})
    else:
        nazov = request.POST.get('nazov')
        popis = request.POST.get('popis')
        konzultant_id = request.POST.get('konzultant')
        odbor_id = request.POST.get('odbor')
        student_id = request.POST.get('student')
        if student_id != "":
            tema = Tema(
                nazov=nazov,
                popis=popis,
                konzultant_id=konzultant_id,
                odbor_id=odbor_id,
                student_id = student_id,
                dostupnost_id=2,
                pocet_konzultacii=0
            )
            tema.save()
        else: 
            tema = Tema(
                nazov=nazov,
                popis=popis,
                konzultant_id=konzultant_id,
                odbor_id=odbor_id,
                dostupnost_id=1,
                pocet_konzultacii=0
            )
            tema.save()
        return redirect('soc')