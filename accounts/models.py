from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True, editable=True)
    full_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username