# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='social_image',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
