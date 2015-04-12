# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_one_liner'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='backer',
            field=models.BigIntegerField(default=0, null=True, blank=True),
        ),
    ]
