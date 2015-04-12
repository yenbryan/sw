# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='one_liner',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
