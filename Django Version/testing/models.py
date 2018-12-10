from django.db import models

# Create your models here.
class Sliders(models.Model):
    slider1 = models.CharField(max_length=200)
    