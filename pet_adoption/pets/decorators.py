from django.core.exceptions import PermissionDenied
from functools import wraps

def group_required(group_name):
    """
    Decorator to check if the user belongs to a specific group.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("You do not have permission to view this page.")
        return _wrapped_view
    return decorator
