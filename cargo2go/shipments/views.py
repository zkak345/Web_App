from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from accounts.decorators import group_required
from .models import Shipments
from .forms import ShipmentForms
from django.http import HttpResponseForbidden

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


@login_required
@group_required("Driver")
def driver_shipments(request):
    shipments = Shipments.objects.filter(assigned_driver=request.user)
    return render(request, "driverlist.html", {"shipments": shipments})

@login_required
@group_required("Driver")
def driver_mark_delivered(request, tracking_id):
    shipment = get_object_or_404(Shipments, tracking_id=tracking_id, assigned_driver=request.user)
    if request.method == 'POST':
        if shipment.status in ["IN_TRANSIT", "OUT_FOR_DELIVERY"]:
            shipment.status = "DELIVERED"
            shipment.save()
        return redirect("driver_shipments")
    return HttpResponseForbidden("Invalid Request")


@login_required
@group_required("Customer")
def customer_shipments(request):
    shipments = Shipments.objects.filter(customer = request.user)
    return render(request, "customerlist.html", {"shipments": shipments})
# Create your views here.


