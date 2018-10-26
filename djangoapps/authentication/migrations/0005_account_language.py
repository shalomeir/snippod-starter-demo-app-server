# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20150922_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='language',
            field=models.CharField(max_length=5, default='en', verbose_name='language'),
        ),
    ]
