# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150801_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herolevel',
            name='training_time',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
