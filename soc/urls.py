from django.urls import path
from . import views

urlpatterns = [
    path('', views.vypis_temy, name='soc'),
]
