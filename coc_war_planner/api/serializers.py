from rest_framework import serializers
from coc_war_planner.core.models import Clan
from coc_war_planner.core.models import Member
from coc_war_planner.core.models import Troop
from coc_war_planner.core.models import TroopLevel
from coc_war_planner.core.models import Troops


class ClanSerializer(serializers.ModelSerializer):

    chief = serializers.PrimaryKeyRelatedField(required=True, queryset=Member.objects.filter(clan=None))

    class Meta:
        model = Clan
        fields = ('id', 'chief', 'name', 'pin', 'location', 'level')

    def save(self, instance, validated_data):
        chief = validated_data.get('chief')
        # Check if the chief is already chief of another clan
        if chief.clan or chief.is_chief():
            raise serializers.ValidationError({
                'chief': "The chief can't be part in another clan"
            })

        return super(ClanSerializer, self).save(instance, validated_data)

class ClanPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clan
        fields = ('id', 'chief', 'name', 'pin', 'location', 'level')

    def get_fields(self, *args, **kwargs):
        fields = super(ClanPutSerializer, self).get_fields(*args, **kwargs)
        fields['chief'].queryset = self.instance.members.all()
        return fields

    def update(self, instance, validated_data):
        chief = validated_data.get('chief')
        if chief not in instance.members.all():
            raise serializers.ValidationError({
                'chief': "The new chief must be part of the clan"
            })

        return super(ClanPutSerializer, self).update(instance, validated_data)


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('id', 'level', 'clan')


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
        troop_level = validated_data.get('troop_level')
        troop = validated_data.get('troop')
        if troop_level.troop != troop:
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
        if instance.troop != troop_level.troop:
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

