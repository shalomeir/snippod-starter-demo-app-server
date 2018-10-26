# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20160211_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=300, help_text='User introduction', verbose_name='description', blank=True),
        ),
    ]
