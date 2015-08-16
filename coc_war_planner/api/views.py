from coc_war_planner.api.permissions import CreateNotAllowed
from coc_war_planner.api.permissions import IsChiefOrReadOnly
from coc_war_planner.api.permissions import IsUserOrReadOnly
from coc_war_planner.api.permissions import IsOwnerOrReadOnly
from coc_war_planner.api.permissions import IsNotPartOfClanOrCreateNotAllowed

from coc_war_planner.api.serializers import ClanSerializer
from coc_war_planner.api.serializers import ClanPutSerializer
from coc_war_planner.api.serializers import MemberSerializer
from coc_war_planner.api.serializers import TroopsPostSerializer
from coc_war_planner.api.serializers import TroopsPutSerializer
from coc_war_planner.api.serializers import TroopsGetSerializer

from coc_war_planner.core.models import Clan
from coc_war_planner.core.models import Member
from coc_war_planner.core.models import Troops
from coc_war_planner.core.models import TroopLevel

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets

class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsChiefOrReadOnly,
            IsNotPartOfClanOrCreateNotAllowed)

    def perform_create(self, serializer):
        instance = serializer.save(chief=self.request.user.member)
        request.user.member.clan = instance
        request.user.member.save()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return ClanPutSerializer

        return ClanSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            CreateNotAllowed,
            IsUserOrReadOnly,)


class TroopsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TroopsPostSerializer
        elif self.request.method == 'PUT':
            return TroopsPutSerializer

        return TroopsGetSerializer

    def get_queryset(self):
        member_id = self.request.GET.get('member_id', self.request.user.member.id)
        if member_id is None:
            raise serializers.ValidationError({
                'member_id': 'Parameter is missing.'
            })

        troops = Troops.objects.filter(member_id=member_id)

        troops_id = self.kwargs.get(self.lookup_field)
        if troops_id:
            troops = troops.filter(pk=troops_id)

        return troops

