# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150801_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herolevel',
            name='ability_level',
            field=models.ForeignKey(to='core.HeroAbility', null=True),
        ),
    ]
