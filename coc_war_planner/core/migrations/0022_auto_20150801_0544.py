# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150801_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trooplevel',
            name='damage_per_attack',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trooplevel',
            name='damage_per_second',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
