# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='bought',
            new_name='coming',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='price',
            new_name='guests',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='item',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='location',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='store',
        ),
        migrations.AddField(
            model_name='entry',
            name='diet',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='email',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='message',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='songrequest',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='img',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
