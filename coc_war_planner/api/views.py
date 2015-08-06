from coc_war_planner.api.permissions import IsChiefOrReadOnly
from coc_war_planner.api.permissions import IsUserOrReadOnly
from coc_war_planner.api.serializers import ClanSerializer
from coc_war_planner.api.serializers import MemberSerializer
from coc_war_planner.core.models import Clan
from coc_war_planner.core.models import Member


from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets

class ClanViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsChiefOrReadOnly,)

    def perform_create(self, serializer):
            serializer.save(chief=self.request.user)

class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsUserOrReadOnly,)
