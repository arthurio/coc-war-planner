# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_member_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='chief',
            field=models.ForeignKey(related_name='+', to='core.Member', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='clan',
            field=models.ForeignKey(related_name='members', blank=True, to='core.Clan', null=True),
        ),
    ]
