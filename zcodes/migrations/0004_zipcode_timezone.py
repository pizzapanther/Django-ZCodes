# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zcodes', '0003_auto_20150520_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='zipcode',
            name='timezone',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
