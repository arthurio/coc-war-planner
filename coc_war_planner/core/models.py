from django.db import models
from django.contrib.auth.models import User

from gettext import gettext as _

from coc_war_planner.core.fields import JSONField


class Clan(models.Model):
    name = models.CharField(max_length=50)
    pin = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    level = models.IntegerField()


class Member(User):
    user = models.OneToOneField(User)
    level = models.IntegerField()
    clan = models.ForeignKey(Clan)


class Troop(models.Model):

    TIER_1 = 't1'
    TIER_2 = 't2'
    TIER_3 = 't3'
    DARK = 'd'

    CATEGORIES = (
        (TIER_1, _("tier 1")),
        (TIER_2, _("tier 2")),
        (TIER_3, _("tier 3")),
        (DARK, _("dark")),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    preferred_target = models.CharField(max_length=250)
    attack_type = models.CharField(max_length=250)
    housing_space = models.IntegerField()
    training_time = models.IntegerField()  # in seconds
    barack_level_required = models.CharField(max_length=250)
    range = models.IntegerField()
    movement_speed = models.IntegerField()
    attack_speed = models.IntegerField()
    extra_data = JSONField(null=True)


class TroopLevel(models.Model):
    troop = models.ForeignKey(Troop)
    level = models.IntegerField()
    training_cost = models.IntegerField()  # in gold
    research_time = models.IntegerField()  # in seconds
    research_cost = models.IntegerField()  # in gold
    laboratory_level_required = models.IntegerField()
    hitpoints = models.IntegerField()
    damage_per_second = models.IntegerField()
    damage_per_attack = models.IntegerField()
    extra_data = JSONField(null=True)

    class Meta:
        unique_together = ('troop', 'level')


class Troops(models.Model):
    user = models.ForeignKey(Member)
    troop = models.ForeignKey(Troop)
    troop_level = models.ForeignKey(TroopLevel)

    class Meta:
        unique_together = ('user', 'troop')


class Spell(models.Model):

    REGULAR = "r"
    DARK = "d"

    CATEGORIES = (
        (REGULAR, _("regular")),
        (DARK, _("dark")),
    )
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    radius = models.IntegerField()
    number_of_pulses = models.IntegerField()
    time_between_pulses = models.IntegerField()  # in seconds
    housing_space = models.IntegerField()
    time_to_brew = models.IntegerField()  # in seconds
    target = models.CharField(max_length=250)
    spell_factory_level_required = models.IntegerField()
    extra_data = JSONField(null=True)


class SpellLevel(models.Model):

    spell = models.ForeignKey(Spell)
    level = models.IntegerField()
    cost = models.IntegerField()  # in gold
    research_cost = models.IntegerField()  # in gold
    research_time = models.IntegerField()  # in seconds
    laboratory_level_required = models.CharField(max_length=250)
    extra_data = JSONField(null=True)

    class Meta:
        unique_together = ('spell', 'level')


class Spells(models.Model):
    user = models.ForeignKey(Member)
    spell = models.ForeignKey(Troop)
    spell_level = models.ForeignKey(TroopLevel)

    class Meta:
        unique_together = ('user', 'spell')


class Hero(models.Model):
    name = models.CharField(max_length=50)
    attack_type = models.CharField(max_length=250)
    movement_speed = models.IntegerField()  # in seconds
    attack_speed = models.IntegerField()  # in seconds
    range = models.IntegerField()
    search_radius = models.IntegerField()


class HeroAbility(models.Model):
    damage_increase = models.IntegerField()
    health_recovery = models.IntegerField()
    ability_time = models.IntegerField()  # in seconds
    summoned_unites = models.IntegerField()
    extra_data = JSONField(null=True)


class HeroLevel(models.Model):
    hero = models.ForeignKey(Hero)
    level = models.IntegerField()
    damage_per_second = models.IntegerField()
    damage_per_hit = models.IntegerField()
    hitpoints = models.IntegerField()
    regeneration_time = models.IntegerField()  # in seconds
    ability_level = models.ForeignKey(HeroAbility)
    training_cost = models.IntegerField()  # in gold
    training_time = models.IntegerField()  # in seconds
    town_hall_level_required = models.IntegerField()

    class Meta:
        unique_together = ('hero', 'level')


class Heros(models.Model):
    user = models.ForeignKey(Member)
    hero = models.ForeignKey(Hero)
    hero_level = models.ForeignKey(HeroLevel)

    class Meta:
        unique_together = ('user', 'hero')

class TownHall(models.Model):
    user = models.ForeignKey(Member)
    level = models.IntegerField()


class War(models.Model):
    clan = models.ForeignKey(Clan)
    enemy_clan = models.CharField(max_length=100)
    number_of_participants = models.IntegerField()
    members = models.ManyToManyField(User)
    preparation_time_remaining = models.IntegerField()  # in seconds
    time_remaining = models.IntegerField()  # in seconds


class Attack(models.Model):

    FIRST = "1"
    SECOND = "2"

    ITERATIONS = (
        (FIRST, _("first")),
        (SECOND, _("second")),
    )

    war = models.ForeignKey(War)
    member = models.ForeignKey(Member)
    enemy_rank = models.IntegerField()
    enemy_town_hall_level = models.IntegerField()
    stars = models.IntegerField()
    durations = models.IntegerField()  # in seconds
    iteration = models.CharField(max_length=1, choices=ITERATIONS)
