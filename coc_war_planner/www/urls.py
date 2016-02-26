from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from coc_war_planner.www.views import NonAdminTemplateView

urlpatterns = [
    url(r'^register/$',
        NonAdminTemplateView.as_view(template_name='registration/register.html'),
        name='registration.register'
        ),
    url(r'^login/$',
        NonAdminTemplateView.as_view(template_name='registration/register.html'),
        name='registration.login'),
    url(
        r'^dashboard/$',
        login_required(
            NonAdminTemplateView.as_view(
                template_name='www/dashboard.html'
            )
         ),
        name='www.dashboard'
    ),
    url(
        r'^profile/$',
        login_required(
            NonAdminTemplateView.as_view(
                template_name='www/profile.html'
            )
        ),
        name='www.profile'
    ),
    url(r'^$', NonAdminTemplateView.as_view(template_name='home.html'), name='home'),
]
