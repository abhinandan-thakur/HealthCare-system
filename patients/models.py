from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)