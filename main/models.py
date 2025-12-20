
from django.db import models


class User(models.Model):
    # Поля из твоей SQLite таблицы
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)  # email должен быть уникальным
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"