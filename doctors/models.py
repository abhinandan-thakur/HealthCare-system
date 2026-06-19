from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    # in years
    work_experience = models.PositiveIntegerField()
    room_number = models.CharField(max_length=50)
    date_of_joining = models.DateTimeField(auto_now_add=True)
