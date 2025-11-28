from django.contrib import admin
from django.urls import path, include
from main.views import index, login_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),

    path('clients_db/', include('clients_db.urls')),
    path('casino/', include('casino.urls')),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]
