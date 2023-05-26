from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField("Telefon raqamlar", max_length=10)