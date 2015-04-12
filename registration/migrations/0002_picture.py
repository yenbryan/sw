# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'media/profile_pictures', blank=True)),
                ('description', models.CharField(max_length=140, null=True, blank=True)),
                ('profile', models.ForeignKey(related_name='pictures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
