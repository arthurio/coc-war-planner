# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150801_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='spell_factory_level_required',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
