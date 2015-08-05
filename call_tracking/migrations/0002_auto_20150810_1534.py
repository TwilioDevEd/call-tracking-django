# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadsource',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
