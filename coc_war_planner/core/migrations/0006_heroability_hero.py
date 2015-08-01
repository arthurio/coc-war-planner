# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150801_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroability',
            name='hero',
            field=models.ForeignKey(default=2, to='core.Hero'),
            preserve_default=False,
        ),
    ]
