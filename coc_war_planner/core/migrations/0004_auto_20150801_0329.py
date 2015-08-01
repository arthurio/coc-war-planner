# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_heroability_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroability',
            name='ability_time',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
