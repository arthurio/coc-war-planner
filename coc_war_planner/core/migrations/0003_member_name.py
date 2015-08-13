# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
