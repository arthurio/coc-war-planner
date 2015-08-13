# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enemy_rank', models.IntegerField()),
                ('enemy_town_hall_level', models.IntegerField()),
                ('stars', models.IntegerField()),
                ('durations', models.IntegerField()),
                ('iteration', models.CharField(max_length=1, choices=[(b'1', b'first'), (b'2', b'second')])),
            ],
        ),
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('attack_type', models.CharField(max_length=250)),
                ('movement_speed', models.DecimalField(max_digits=5, decimal_places=2)),
                ('attack_speed', models.DecimalField(max_digits=5, decimal_places=2)),
                ('range', models.IntegerField()),
                ('search_radius', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroAbility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('damage_increase', models.IntegerField()),
                ('health_recovery', models.IntegerField()),
                ('ability_time', models.DecimalField(max_digits=5, decimal_places=2)),
                ('summoned_unites', models.IntegerField()),
                ('extra_data', annoying.fields.JSONField(null=True, blank=True)),
                ('hero', models.ForeignKey(to='core.Hero')),
            ],
        ),
        migrations.CreateModel(
            name='HeroLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('damage_per_second', models.IntegerField()),
                ('damage_per_hit', models.DecimalField(max_digits=5, decimal_places=2)),
                ('hitpoints', models.IntegerField()),
                ('regeneration_time', models.IntegerField()),
                ('training_cost', models.IntegerField()),
                ('training_time', models.IntegerField(null=True, blank=True)),
                ('town_hall_level_required', models.IntegerField()),
                ('ability_level', models.ForeignKey(blank=True, to='core.HeroAbility', null=True)),
                ('hero', models.ForeignKey(to='core.Hero')),
            ],
        ),
        migrations.CreateModel(
            name='Heros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hero', models.ForeignKey(to='core.Hero')),
                ('hero_level', models.ForeignKey(to='core.HeroLevel')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(null=True, blank=True)),
                ('clan', models.ForeignKey(blank=True, to='core.Clan', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=15, choices=[(b'r', b'regular'), (b'd', b'dark')])),
                ('radius', models.DecimalField(max_digits=5, decimal_places=2)),
                ('number_of_pulses', models.IntegerField(null=True, blank=True)),
                ('time_between_pulses', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('housing_space', models.IntegerField()),
                ('time_to_brew', models.IntegerField()),
                ('target', models.CharField(max_length=250, null=True, blank=True)),
                ('spell_factory_level_required', models.IntegerField(null=True, blank=True)),
                ('extra_data', annoying.fields.JSONField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpellLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('research_cost', models.IntegerField(null=True, blank=True)),
                ('research_time', models.IntegerField(null=True, blank=True)),
                ('laboratory_level_required', models.CharField(max_length=250, null=True, blank=True)),
                ('extra_data', annoying.fields.JSONField(null=True, blank=True)),
                ('spell', models.ForeignKey(to='core.Spell')),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', models.ForeignKey(to='core.Member')),
            ],
        ),
        migrations.CreateModel(
            name='TownHall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('member', models.ForeignKey(to='core.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Troop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=10, choices=[(b't1', b'tier 1'), (b't2', b'tier 2'), (b't3', b'tier 3'), (b'd', b'dark')])),
                ('preferred_target', models.CharField(max_length=250, null=True, blank=True)),
                ('attack_type', models.CharField(max_length=250)),
                ('housing_space', models.IntegerField()),
                ('training_time', models.IntegerField()),
                ('barack_level_required', models.CharField(max_length=250)),
                ('range', models.DecimalField(max_digits=5, decimal_places=2)),
                ('movement_speed', models.DecimalField(max_digits=5, decimal_places=2)),
                ('attack_speed', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('extra_data', annoying.fields.JSONField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TroopLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('damage_per_second', models.IntegerField(null=True, blank=True)),
                ('damage_per_attack', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('hitpoints', models.IntegerField()),
                ('training_cost', models.IntegerField()),
                ('research_cost', models.IntegerField(null=True, blank=True)),
                ('laboratory_level_required', models.IntegerField(null=True, blank=True)),
                ('research_time', models.IntegerField(null=True, blank=True)),
                ('extra_data', annoying.fields.JSONField(null=True, blank=True)),
                ('troop', models.ForeignKey(to='core.Troop')),
            ],
        ),
        migrations.CreateModel(
            name='Troops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('member', models.ForeignKey(to='core.Member')),
                ('troop', models.ForeignKey(to='core.Troop')),
                ('troop_level', models.ForeignKey(to='core.TroopLevel')),
            ],
        ),
        migrations.CreateModel(
            name='War',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enemy_clan', models.CharField(max_length=100)),
                ('number_of_participants', models.IntegerField()),
                ('preparation_time_remaining', models.IntegerField()),
                ('time_remaining', models.IntegerField()),
                ('clan', models.ForeignKey(to='core.Clan')),
                ('members', models.ManyToManyField(to='core.Member')),
            ],
        ),
        migrations.AddField(
            model_name='spells',
            name='spell',
            field=models.ForeignKey(to='core.Troop'),
        ),
        migrations.AddField(
            model_name='spells',
            name='spell_level',
            field=models.ForeignKey(to='core.TroopLevel'),
        ),
        migrations.AddField(
            model_name='heros',
            name='member',
            field=models.ForeignKey(to='core.Member'),
        ),
        migrations.AddField(
            model_name='clan',
            name='chief',
            field=models.ForeignKey(related_name='+', to='core.Member'),
        ),
        migrations.AddField(
            model_name='attack',
            name='member',
            field=models.ForeignKey(to='core.Member'),
        ),
        migrations.AddField(
            model_name='attack',
            name='war',
            field=models.ForeignKey(to='core.War'),
        ),
        migrations.AlterUniqueTogether(
            name='troops',
            unique_together=set([('member', 'troop')]),
        ),
        migrations.AlterUniqueTogether(
            name='trooplevel',
            unique_together=set([('troop', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='spells',
            unique_together=set([('member', 'spell')]),
        ),
        migrations.AlterUniqueTogether(
            name='spelllevel',
            unique_together=set([('spell', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='heros',
            unique_together=set([('member', 'hero')]),
        ),
        migrations.AlterUniqueTogether(
            name='herolevel',
            unique_together=set([('hero', 'level')]),
        ),
    ]
