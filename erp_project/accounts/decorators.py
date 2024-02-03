from django.contrib import messages
from django.shortcuts import redirect
from functools import wraps


def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "You do not have permission to access this dashboard.")
                return redirect('user_login')

        return _wrapped_view

    return decorator
