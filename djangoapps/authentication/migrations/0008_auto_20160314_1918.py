# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20160211_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and ./+/-/_ only.', verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.+-]+$', 'Enter a valid username.', 'invalid')]),
        ),
    ]
