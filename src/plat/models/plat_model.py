from django.db import models

# Create your models here.

class Plat(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.name
