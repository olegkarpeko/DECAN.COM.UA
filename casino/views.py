from django.shortcuts import render
from django.http import JsonResponse
from .models import CasinoResult
from clients_db.models import Client_poslugs
import random

symbols = ["spintal", "barranic", "vozniak", "dekan", "kyrator"]

WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def casino(request):
    return render(request, "casino/casic.html")


def spin(request):
    if request.method == "POST":
        input_name = request.POST.get("user_name", "").strip()

        # якщо юзер залогінений — беремо username/email з акаунта
        if request.user.is_authenticated:
            user_for_fk = request.user
            user_name = request.user.username
            email = request.user.email or None
        else:
            user_for_fk = None
            user_name = input_name or "Гравець"
            email = None

        # генеруємо 3x3 як плоский список з 9 символів
        slot_flat = [random.choice(symbols) for _ in range(9)]

        # виграш по лініях
        won = any(
            slot_flat[a] == slot_flat[b] == slot_flat[c]
            for (a, b, c) in WIN_LINES
        )

        if won:
            outcome = "Декан закриває рік"
            posluga_value = "закрити рік"
        else:
            outcome = "Перездача"
            posluga_value = "перездача"

        # ✅ пишемо в Client_poslugs ДЛЯ КОНКРЕТНОГО ЮЗЕРА
        Client_poslugs.objects.create(
            user=user_for_fk,
            name=user_name,
            email=email,
            phone="",
            posluga=posluga_value,
        )

        # історія казино
        CasinoResult.objects.create(
            user=user_for_fk,
            user_name=user_name,
            result=outcome,
        )

        return JsonResponse({"slot": slot_flat, "outcome": outcome})
