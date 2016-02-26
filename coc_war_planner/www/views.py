from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from coc_war_planner.www.decorators import redirect_to_admin_if_superuser


class NonAdminTemplateView(TemplateView):

    @method_decorator(redirect_to_admin_if_superuser)
    def get(self, request):
        return super(NonAdminTemplateView, self).get(request)
