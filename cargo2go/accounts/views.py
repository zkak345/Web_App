from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    groups = set(request.user.groups.values_list("name", flat=True))
    if "Admin" in groups or "Manager" in groups:
        template = "manager.html"
    elif "Driver" in groups:
        template = "driver.html"
    else:
        return redirect("customer_shipments")
    
    context = {
        "user": request.user,
        "groups": groups,
    }

    return render(request, template, context)
# Create your views here.
