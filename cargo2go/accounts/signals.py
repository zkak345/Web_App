from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver 

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    roles = {"Admin": Permission.objects.all(),
             "Manager": Permission.objects.filter(content_type__app_label__in=["shipments", "warehouses"]), 
             "Driver": Permission.objects.filter(content_type__app_label__in="shipments", codename__in=["change_shipment"]),
             "Customer": []}
    for role, permission1 in roles.items():
        group, created = Group.objects.get_or_create(name=role)
        group.permissions.set(permission1)
        group.save()

