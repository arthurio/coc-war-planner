from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/$', TemplateView.as_view(template_name='registration/register.html'), name='register'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
]
