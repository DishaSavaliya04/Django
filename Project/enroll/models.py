from django.db import models

# Create your models here.
class student(models.Model):
    studid=models.IntegerField()
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=70)

def __str__(self):
    return str(self.studid)
