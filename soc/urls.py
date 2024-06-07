from django.urls import path
from . import views

urlpatterns = [
    path('', views.vypis_temy, name='soc'),
    path('temy/<tema>/', views.vypis_temu, name='tema'),
    path('ucitel/<ucitel>/', views.vypis_ucitela, name='ucitel'),
    path('student/<student>/', views.vypis_studenta, name='student'),
    path('statistika/', views.vypis_statistiku, name='statistika'),
]
