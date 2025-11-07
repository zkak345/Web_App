from django.db import models

class Warehouse(models.Model):
    name = models.CharField()
    address = models.TextField

    def __str__(self):
        return self.name
# Create your models here.
