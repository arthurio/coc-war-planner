# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import coc_war_planner.core.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('movement_speed', models.IntegerField()),
                ('attack_speed', models.IntegerField()),
                ('range', models.IntegerField()),
                ('search_radius', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HeroAbility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('damage_increase', models.IntegerField()),
                ('health_recovery', models.IntegerField()),
                ('ability_time', models.IntegerField()),
                ('summoned_unites', models.IntegerField()),
                ('extra_data', coc_war_planner.core.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('damage_per_second', models.IntegerField()),
                ('damage_per_hit', models.IntegerField()),
                ('hitpoints', models.IntegerField()),
                ('regeneration_time', models.IntegerField()),
                ('training_cost', models.IntegerField()),
                ('training_time', models.IntegerField()),
                ('town_hall_level_required', models.IntegerField()),
                ('ability_level', models.ForeignKey(to='core.HeroAbility')),
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
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('level', models.IntegerField()),
                ('clan', models.ForeignKey(to='core.Clan')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=15, choices=[(b'r', b'regular'), (b'd', b'dark')])),
                ('radius', models.IntegerField()),
                ('number_of_pulses', models.IntegerField()),
                ('time_between_pulses', models.IntegerField()),
                ('housing_space', models.IntegerField()),
                ('time_to_brew', models.IntegerField()),
                ('target', models.CharField(max_length=250)),
                ('spell_factory_level_required', models.IntegerField()),
                ('extra_data', coc_war_planner.core.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpellLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('research_cost', models.IntegerField()),
                ('research_time', models.IntegerField()),
                ('laboratory_level_required', models.CharField(max_length=250)),
                ('extra_data', coc_war_planner.core.fields.JSONField(null=True)),
                ('spell', models.ForeignKey(to='core.Spell')),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='TownHall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('user', models.ForeignKey(to='core.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Troop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=10, choices=[(b't1', b'tier 1'), (b't2', b'tier 2'), (b't3', b'tier 3'), (b'd', b'dark')])),
                ('preferred_target', models.CharField(max_length=250)),
                ('attack_type', models.CharField(max_length=250)),
                ('housing_space', models.IntegerField()),
                ('training_time', models.IntegerField()),
                ('barack_level_required', models.CharField(max_length=250)),
                ('range', models.IntegerField()),
                ('movement_speed', models.IntegerField()),
                ('attack_speed', models.IntegerField()),
                ('extra_data', coc_war_planner.core.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TroopLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('training_cost', models.IntegerField()),
                ('research_time', models.IntegerField()),
                ('research_cost', models.IntegerField()),
                ('laboratory_level_required', models.IntegerField()),
                ('hitpoints', models.IntegerField()),
                ('damage_per_second', models.IntegerField()),
                ('damage_per_attack', models.IntegerField()),
                ('extra_data', coc_war_planner.core.fields.JSONField(null=True)),
                ('troop', models.ForeignKey(to='core.Troop')),
            ],
        ),
        migrations.CreateModel(
            name='Troops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('troop', models.ForeignKey(to='core.Troop')),
                ('troop_level', models.ForeignKey(to='core.TroopLevel')),
                ('user', models.ForeignKey(to='core.Member')),
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
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
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
            model_name='spells',
            name='user',
            field=models.ForeignKey(to='core.Member'),
        ),
        migrations.AddField(
            model_name='heros',
            name='user',
            field=models.ForeignKey(to='core.Member'),
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
            unique_together=set([('user', 'troop')]),
        ),
        migrations.AlterUniqueTogether(
            name='trooplevel',
            unique_together=set([('troop', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='spells',
            unique_together=set([('user', 'spell')]),
        ),
        migrations.AlterUniqueTogether(
            name='spelllevel',
            unique_together=set([('spell', 'level')]),
        ),
        migrations.AlterUniqueTogether(
            name='heros',
            unique_together=set([('user', 'hero')]),
        ),
        migrations.AlterUniqueTogether(
            name='herolevel',
            unique_together=set([('hero', 'level')]),
        ),
    ]
