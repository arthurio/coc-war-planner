from coc_war_planner.api import views

from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'clans', views.ClanViewSet)
router.register(r'members', views.MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]

