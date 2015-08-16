# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150815_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='clan',
            name='pin',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
