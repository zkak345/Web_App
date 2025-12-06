from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    groups = set(request.user.groups.values_list("name", flat=True))
    if "Admin" in groups or "Manager" in groups:
        template = "manager.html"
    elif "Driver" in groups:
        template = "accounts/driver_home.html"
    else:
        template = "accounts/customer.html"
    
    context = {
        "user": request.user,
        "groups": groups,
    }

    return render(request, template, context)
# Create your views here.
