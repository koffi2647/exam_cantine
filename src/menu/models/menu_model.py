from django.db import models

from plat.models.plat_model import Plat
# Create your models here.

class Menu(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    creation_date = models.DateField()
    plat = models.OneToOneField(Plat, on_delete=models.CASCADE, related_name='menu')

    def __str__(self):
        return f"Menu {self.id} - {self.creation_date}"
