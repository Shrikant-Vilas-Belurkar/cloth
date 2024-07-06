from django.db import models

# Create your models here.
class Black(models.Model):
    Tshirt = models.CharField(max_length=25)
    Size = models.CharField(max_length=25)
    Color = models.CharField(max_length=25)
