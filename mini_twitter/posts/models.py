from django.db import models


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}: {self.title}'


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} to {self.post.title}'
