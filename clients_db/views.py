from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client_poslugs


@login_required
def clients_db(request):
    # тільки записи цього юзера
    orders = (
        Client_poslugs.objects
        .filter(user=request.user)
        .order_by("-id")
    )

    total_orders = orders.count()
    loses_count = orders.filter(posluga="перездача").count()
    wins_count = total_orders - loses_count

    return render(
        request,
        "clients_db/index.html",
        {
            "clients": orders,
            "total_orders": total_orders,
            "loses_count": loses_count,
            "wins_count": wins_count,
        },
    )
