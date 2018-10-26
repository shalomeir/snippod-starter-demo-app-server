# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_account_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=300, help_text='User introduction', default=datetime.datetime(2016, 2, 11, 13, 14, 37, 280358, tzinfo=utc), verbose_name='description'),
            preserve_default=False,
        ),
    ]
