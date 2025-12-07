from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from .models import Shipments
from .forms import ShipmentForms

@login_required
@group_required("Manager", "Admin")
def manager_shipment_list(request):
    shipments = Shipments.objects.all()
    return render(request, "managerlist.html", {"Shipments": shipments})

@login_required
@group_required("Manager", "Admin")
def manager_shipment_create(request):
    if request.method == "POST":
        form = ShipmentForms(request.POST)
        if form.isvalid():
            form.save()
            return redirect("manager_shipments")
    else:
        form = ShipmentForms()
    return render(request, "manager_create.html", {"form": form})

# Create your views here.
