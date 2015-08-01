# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_heroability_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroability',
            name='extra_data',
            field=annoying.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spell',
            name='extra_data',
            field=annoying.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='spelllevel',
            name='extra_data',
            field=annoying.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='troop',
            name='extra_data',
            field=annoying.fields.JSONField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='trooplevel',
            name='extra_data',
            field=annoying.fields.JSONField(null=True, blank=True),
        ),
    ]
