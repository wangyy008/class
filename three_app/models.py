from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=8)
    age = models.IntegerField()
    sex = models.IntegerField()
    