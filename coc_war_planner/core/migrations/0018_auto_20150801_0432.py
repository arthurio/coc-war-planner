# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150801_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spelllevel',
            name='research_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spelllevel',
            name='research_time',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
