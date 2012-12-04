from django.db import models

class Product(models.Model):
    hs = models.CharField(max_length=8, unique=True)
