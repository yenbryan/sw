# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150412_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
