from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now_add=True)

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # related_name : 역참조시 이름 바꿈