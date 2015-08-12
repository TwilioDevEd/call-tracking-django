# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeadSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('incoming_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
                ('forwarding_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('source', models.ForeignKey(to='call_tracking.LeadSource')),
            ],
        ),
    ]
