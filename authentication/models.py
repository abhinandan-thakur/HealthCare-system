from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [("ADMIN", "ADMIN"), ("DOCTOR", "DOCTOR"), ("PATIENT", "PATIENT")]
    phone_no = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)