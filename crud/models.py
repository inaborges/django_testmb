from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    birthday_date = models.DateField(blank=True,null=True)
    text = models.TextField(blank=True,null=True)


