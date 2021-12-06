from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    url = models.URLField()
