# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150801_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='radius',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
