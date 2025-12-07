from django import forms
from .models import Shipments

class ShipmentForms(forms.ModelForm):
    class Meta:
        model = Shipments
        fields = ["shipment_name", "tracking_id", "destination", "assigned_driver", "status", "customer"]

    def clean_destination(self):
        dest = self.cleaned_data["destination"]
        if len(dest.strip()) < 10 or len(dest.strip()) > 50:
            raise forms.ValidationError("Destination must be atleast 10 char and less than 50")
        return dest