# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20150801_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='number_of_pulses',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='time_between_pulses',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
