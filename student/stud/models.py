from django.db import models

# Create your models here.
class Stud(models.Model):
    name=models.CharField(max_length=100)
    marks=models.IntegerField(null=True)
    rollno=models.IntegerField(null=True)

