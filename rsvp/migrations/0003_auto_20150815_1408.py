# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_auto_20150815_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]
