from django.db import models
from django.conf import settings
# Create your models here.
class Recipiant(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.fname}, {self.lname}"

#Create the Appointment
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
