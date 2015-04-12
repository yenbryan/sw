# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_picture_social_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
