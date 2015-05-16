# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('bought', models.BooleanField()),
                ('img', models.FileField(upload_to=b'')),
            ],
        ),
    ]
