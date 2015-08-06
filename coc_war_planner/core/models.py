from annoying.fields import AutoOneToOneField

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from gettext import gettext as _

from annoying.fields import JSONField


class Clan(models.Model):
    chief = models.ForeignKey('Member', related_name="+")
    name = models.CharField(max_length=50)
    pin = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    level = models.IntegerField()


class Member(User):
    user = models.OneToOneField(User)
    level = models.IntegerField(null=True, blank=True)
    clan = models.ForeignKey(Clan, null=True, blank=True)

def create_member(sender, instance, created, **kwargs):
    if created and instance.is_superuser is False:
        Member.objects.create(user=instance)

post_save.connect(create_member, sender=User)


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
    preferred_target = models.CharField(max_length=250, blank=True, null=True)
    attack_type = models.CharField(max_length=250)
    housing_space = models.IntegerField()
    training_time = models.IntegerField()  # in seconds
    barack_level_required = models.CharField(max_length=250)
    range = models.DecimalField(max_digits=5, decimal_places=2)  # in tile
    movement_speed = models.DecimalField(max_digits=5, decimal_places=2)
    attack_speed = models.DecimalField(max_digits=5, decimal_places=2,
                                       null=True, blank=True)
    extra_data = JSONField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class TroopLevel(models.Model):
    troop = models.ForeignKey(Troop)
    level = models.IntegerField()
    damage_per_second = models.IntegerField(null=True, blank=True)
    damage_per_attack = models.DecimalField(max_digits=6, decimal_places=2,
                                            null=True, blank=True)
    hitpoints = models.IntegerField()
    training_cost = models.IntegerField()  # in gold
    research_cost = models.IntegerField(null=True, blank=True)  # in gold
    laboratory_level_required = models.IntegerField(null=True, blank=True)
    research_time = models.IntegerField(null=True, blank=True)  # in seconds
    extra_data = JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('troop', 'level')

    def __unicode__(self):
        return "%s - Level %s" % (self.troop, self.level)


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
    radius = models.DecimalField(max_digits=5, decimal_places=2)  # in tile
    number_of_pulses = models.IntegerField(blank=True, null=True)
    time_between_pulses = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # in seconds
    housing_space = models.IntegerField()
    time_to_brew = models.IntegerField()  # in seconds
    target = models.CharField(max_length=250, blank=True, null=True)
    spell_factory_level_required = models.IntegerField(blank=True, null=True)
    extra_data = JSONField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class SpellLevel(models.Model):

    spell = models.ForeignKey(Spell)
    level = models.IntegerField()
    cost = models.IntegerField()  # in gold
    research_cost = models.IntegerField(blank=True, null=True)  # in gold
    research_time = models.IntegerField(blank=True, null=True)  # in seconds
    laboratory_level_required = models.CharField(max_length=250, blank=True, null=True)
    extra_data = JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('spell', 'level')

    def __unicode__(self):
        return "%s - Level %s" % (self.spell, self.level)


class Spells(models.Model):
    user = models.ForeignKey(Member)
    spell = models.ForeignKey(Troop)
    spell_level = models.ForeignKey(TroopLevel)

    class Meta:
        unique_together = ('user', 'spell')


class Hero(models.Model):
    name = models.CharField(max_length=50)
    attack_type = models.CharField(max_length=250)
    movement_speed = models.DecimalField(max_digits=5, decimal_places=2)  # in seconds
    attack_speed = models.DecimalField(max_digits=5, decimal_places=2)  # in seconds
    range = models.IntegerField()  # in tiles
    search_radius = models.IntegerField()  # in tiles

    def __unicode__(self):
        return self.name


class HeroAbility(models.Model):
    hero = models.ForeignKey(Hero)
    level = models.IntegerField()
    damage_increase = models.IntegerField()
    health_recovery = models.IntegerField()
    ability_time = models.DecimalField(max_digits=5,
                                       decimal_places=2)  # in seconds
    summoned_unites = models.IntegerField()
    extra_data = JSONField(null=True, blank=True)

    def __unicode__(self):
        return "%s - Level %s" % (self.hero, self.level)


class HeroLevel(models.Model):
    hero = models.ForeignKey(Hero)
    level = models.IntegerField()
    damage_per_second = models.IntegerField()
    damage_per_hit = models.DecimalField(max_digits=5, decimal_places=2)
    hitpoints = models.IntegerField()
    regeneration_time = models.IntegerField()  # in seconds
    ability_level = models.ForeignKey(HeroAbility, null=True, blank=True)
    training_cost = models.IntegerField()  # in gold
    training_time = models.IntegerField(null=True, blank=True)  # in seconds
    town_hall_level_required = models.IntegerField()

    class Meta:
        unique_together = ('hero', 'level')

    def __unicode__(self):
        ability_level = getattr(self.ability_level, 'level', 'N/A')
        return "%s - Level %s - Ability %s" % (self.hero, self.level, ability_level)


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
