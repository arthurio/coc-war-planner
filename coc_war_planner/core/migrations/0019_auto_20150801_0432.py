# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20150801_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spelllevel',
            name='laboratory_level_required',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
