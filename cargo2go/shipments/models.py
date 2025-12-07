from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
class Shipments(models.Model):
    shipment_name = models.CharField(max_length=50)

    Status_choices = [
        ('In_Transit', 'In Transit'),
        ('At_Warehouse', 'At warehouse'),
        ('Deliver', "Out for Delivery"),
        ('Delivered', "Delivered")
    ]
    status = models.CharField(choices=Status_choices, default="At_Warehouse", max_length=20)
    assigned_driver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_shipments")
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="customer_shipments")
    tracking_ID = models.CharField(max_length=20, unique=True, validators=[RegexValidator(regex=r"^[A-Z0-9-]+$", message="Tracking ID input invalid.")])
    destination = models.TextField()
    


    def __str__(self):
        return f"{self.shipment_name} ({self.tracking_ID})"
# Create your models here.
