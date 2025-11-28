# main/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from clients_db.models import Client_poslugs

def index(request):
    if request.method == "POST":
        work_type = request.POST.get("work_type")
        deadline = request.POST.get("deadline")
        contact = request.POST.get("contact")

        # якщо користувач залогінений — пишемо на нього
        user = request.user if request.user.is_authenticated else None

        # мапа типу роботи до "послуги" в твоїй моделі
        if work_type == "Lab Work":
            posluga = "закрити предмет"
        elif work_type == "Coursework":
            posluga = "закрити семестр"
        elif work_type == "Session Closure":
            posluga = "закрити рік"
        else:
            posluga = "інше"

        # ім’я в записі
        if user:
            name = user.username
            email = user.email or ""
        else:
            name = contact or "Гість"
            email = ""

        # створюємо запис у Client_poslugs
        Client_poslugs.objects.create(
            user=user,
            name=name,
            email=email,
            phone=contact,
            posluga=posluga,
        )

        messages.success(request, "Запит збережено! Ми скоро з тобою зв’яжемось.")
        return redirect("home")

    return render(request, "main/index.html")


def login_view(request):
    """Логін користувача."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ви успішно увійшли.")
            return redirect("home")
        else:
            messages.error(request, "Невірний логін або пароль.")
            return redirect("login")

    return render(request, "main/login.html")


def logout_view(request):
    """Вихід з акаунта."""
    logout(request)
    messages.info(request, "Ви вийшли з акаунта.")
    return redirect("home")


def register_view(request):
    """Реєстрація нового користувача."""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Паролі не співпадають.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Такий логін вже зайнятий.")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )

        # одразу логіним
        login(request, user)
        messages.success(request, "Акаунт створено. Ласкаво просимо!")
        return redirect("home")

    return render(request, "main/register.html")
