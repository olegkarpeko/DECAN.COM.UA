from django.db import models
from django.contrib.auth.models import User


class CasinoResult(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="casino_results",
        null=True,
        blank=True,
    )
    user_name = models.CharField(max_length=100)
    result = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} — {self.result}"
