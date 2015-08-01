# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150801_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trooplevel',
            name='laboratory_level_required',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trooplevel',
            name='research_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trooplevel',
            name='research_time',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
