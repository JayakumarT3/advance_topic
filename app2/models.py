from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.DateField()
    password = models.CharField(max_length=30)
    
    