from django.db import models

class Shipments(models.Model):
    shipment_name = models.CharField()

    Status_choices = [
        ('In_Transit', 'In Transit'),
        ('At_Warehouse', 'At warehouse'),
        ('Deliver', "Out for Delivery"),
        ('Delivered', "Delivered")
    ]
    status = models.CharField(choices=Status_choices, default="At_Warehouse")
    assigned_driver = models.CharField()
    tracking_ID = models.TextField()
    destination = models.TextField()


    def __str__(self):
        return self.shipment_name
# Create your models here.
