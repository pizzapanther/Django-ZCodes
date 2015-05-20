# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zcodes', '0002_auto_20150520_1409'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='zipcode',
            unique_together=set([('code', 'country')]),
        ),
    ]
