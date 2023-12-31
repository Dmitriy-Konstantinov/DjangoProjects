from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_joined = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.username}: {self.email}'
