from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from functools import wraps


def redirect_to_admin_if_superuser(func):
    @wraps(func)
    def _wrapped_view(request):
        if request and request.user and request.user.is_superuser:
            return redirect(reverse("admin:index"))

        return func(request)

    return _wrapped_view
