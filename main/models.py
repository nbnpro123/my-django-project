from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)  # email должен быть уникальным
    created_at = models.DateTimeField(auto_now_add=True)  # автоматически добавляет дату создания

    def __str__(self):
        return f"{self.name} ({self.email})"