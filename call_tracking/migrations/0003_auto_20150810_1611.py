# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('call_tracking', '0002_auto_20150810_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leadsource',
            old_name='phone_number',
            new_name='incoming_number',
        ),
        migrations.AddField(
            model_name='leadsource',
            name='forwarding_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]
