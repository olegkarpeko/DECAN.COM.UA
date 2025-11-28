from django.db import models
from django.contrib.auth.models import User


class Client_poslugs(models.Model):
    # хто зробив замовлення / отримав виграш/перездачу
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
        null=True,
        blank=True,
    )

    posluga = models.CharField(max_length=120, default="закрити семестр")
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.posluga == "закрити семестр":
            self.price = 4000
        elif self.posluga == "закрити рік":
            self.price = 7000
        elif self.posluga == "закрити предмет":
            self.price = 700
        elif self.posluga == "перездача":
            self.price = 0
        else:
            self.price = 10000
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.posluga}"
