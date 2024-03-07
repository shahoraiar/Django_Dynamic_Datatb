from django.db import models

# Create your models here.
class user_model(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField(default=True)
