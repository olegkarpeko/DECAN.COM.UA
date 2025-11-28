from django.urls import path
from .views import clients_db

urlpatterns = [
    path("", clients_db, name="clients_db"),


]
