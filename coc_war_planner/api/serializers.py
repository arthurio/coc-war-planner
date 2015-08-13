from rest_framework import serializers
from coc_war_planner.core.models import Clan
from coc_war_planner.core.models import Member
from coc_war_planner.core.models import Troop
from coc_war_planner.core.models import TroopLevel
from coc_war_planner.core.models import Troops


class ClanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ('id', 'name', 'pin', 'location', 'level')


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'user', 'level', 'clan')


class TroopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Troop
        fields = ('name', 'category', 'preferred_target', 'attack_type', 'housing_space', 'training_time', 'barack_level_required', 'range', 'movement_speed', 'attack_speed', 'extra_data')


class TroopLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TroopLevel
        fields = ('level', 'damage_per_second', 'damage_per_attack', 'hitpoints', 'training_cost', 'research_cost', 'laboratory_level_required', 'research_time', 'extra_data')


class TroopsPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Troops
        fields = ('member', 'troop', 'troop_level')

    def create(self, validated_data):
        _filter = {'id': serializer.data.get('troop_level')}
        troop_level = TroopLevel.objects.get(pk=validated_data.get('troop_level'))
        troop = validated_data.get('troop')
        if troop_level.troop_id != troop:
            raise serializers.ValidationError({
                'troop_level': "Must match the selected type of troop."
            })

        return Troops.objects.create(**validated_data)


class TroopsPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Troops
        fields = ('id', 'troop_level',)
        read_only_fields = ('id', 'member', 'troop')

    def update(self, instance, validated_data):
        troop_level = validated_data.get('troop_level')
        if instance.troop.id != troop_level.troop.id:
            raise serializers.ValidationError({
                'troop_level': "Must match the selected type of troop."
            })

        instance.troop_level = troop_level
        instance.save(update_fields=['troop_level'])
        return instance


class TroopsGetSerializer(serializers.ModelSerializer):
    troop = TroopSerializer()
    troop_level = TroopLevelSerializer()

    class Meta:
        model = Troops
        fields = ('id', 'member', 'troop', 'troop_level')

