from rest_framework import serializers
from coc_war_planner.core.models import Clan
from coc_war_planner.core.models import Member


class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ('id', 'name', 'pin', 'location', 'level')

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'user', 'level', 'clan')

