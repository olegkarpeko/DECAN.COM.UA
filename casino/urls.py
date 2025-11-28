from django.urls import path
from .views import casino, spin

urlpatterns = [
    path("", casino, name="casino"),
    path("spin/", spin, name="spin"),
]
