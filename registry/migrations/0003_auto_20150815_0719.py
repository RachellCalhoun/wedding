# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0002_auto_20150516_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
