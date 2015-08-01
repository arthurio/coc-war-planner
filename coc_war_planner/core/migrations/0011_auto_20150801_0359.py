# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150801_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herolevel',
            name='ability_level',
            field=models.ForeignKey(blank=True, to='core.HeroAbility', null=True),
        ),
    ]
