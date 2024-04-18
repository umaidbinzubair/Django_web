from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class post(models.Model):
    title=models.CharField(max_length= 100)
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = request.user

    def __str__(self) -> str:
        return self.title

