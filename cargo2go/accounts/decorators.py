from django.contrib.auth.decorators import  user_passes_test

def group_required(*group_names):
    def in_groups(u):
        if not u.is_authenticated:
            return False
        user_groups = set(u.groups.values_list("name", flat=True))
        return bool(user_groups.intersection(group_names))
    return user_passes_test(in_groups, login_url="login")