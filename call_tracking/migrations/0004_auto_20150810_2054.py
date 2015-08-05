# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('call_tracking', '0003_auto_20150810_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='leadsource',
            name='incoming_number',
            field=phonenumber_field.modelfields.PhoneNumberField(unique=True, max_length=128),
        ),
        migrations.AddField(
            model_name='lead',
            name='source',
            field=models.ForeignKey(to='call_tracking.LeadSource'),
        ),
    ]
