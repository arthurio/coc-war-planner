# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20150801_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troop',
            name='attack_speed',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='troop',
            name='preferred_target',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='troop',
            name='range',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
