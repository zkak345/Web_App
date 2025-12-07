from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from .models import Shipments
from .forms import ShipmentForms

@login_required
@group_required("Manager", "Admin")
def manager_shipment_list(request):
    shipments = Shipments.objects.all()
    return render(request, "managerlist.html", {"shipments": shipments})

@login_required
@group_required("Manager", "Admin")
def manager_shipment_create(request):
    if request.method == "POST":
        form = ShipmentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager_shipments")
    else:
        form = ShipmentForms()
    return render(request, "manager_create.html", {"form": form})

@login_required
@group_required("Manager", "Admin")
def manager_modify_shipment(request, pk):
    shipment = get_object_or_404(Shipments, pk=pk)
    if request.method == "POST":
        form = ShipmentForms(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect("manager_shipments") 
    else:
        form = ShipmentForms(instance=shipment)
    return render(request, "managermodify.html", {"form": form, "shipment": shipment})   

# Create your views here.


