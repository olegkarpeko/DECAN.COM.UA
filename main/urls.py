
from django.urls import path
from . import views



urlpatterns = [
path('', views.index),
path("#services", views.index,name="#services"),
path("#process", views.index,name="#process"),
path("#clients_db", views.index,name="#clients_db"),

]