from django.db import models

# Create your models here.

class Student(models.Model):
    Fast_name=models.CharField( max_length=50)
    Last_name=models.CharField( max_length=50)
    Email=models.EmailField( max_length=254)
    Phone=models.IntegerField()

def __str__(self):
    return self. Fast_name
