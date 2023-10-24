from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.user_id.name} {self.user_id.surname}'


class Comment(models.Model):
    text = models.TextField()
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id.name} {self.user_id.surname}'s comment"
