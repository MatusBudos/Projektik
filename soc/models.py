from django.db import models


class Ucitel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]

class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    heslo = models.CharField(max_length=32)
    trieda = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"] 
       
class Odbor(models.Model):
    nazov = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory" 

class Dostupnost(models.Model):
    nazov = models.CharField(max_length = 25)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Dostupnosť"
        verbose_name_plural = "Dostupnosť" 

class Tema(models.Model):
    nazov = models.CharField(max_length=40)
    popis = models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    odbor = models.ForeignKey(Odbor, on_delete=models.SET_NULL, null=True)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.SET_NULL, null=True)
    pocet_konzultacii = models.IntegerField()

    def __str__(self):
        return f"{self.nazov} {self.dostupnost}"
    
    class Meta:
        verbose_name = "Téma"
        verbose_name_plural = "Témy" 