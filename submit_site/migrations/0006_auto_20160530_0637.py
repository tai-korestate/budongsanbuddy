# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-30 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_site', '0005_auto_20160530_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='pics2',
            field=models.FileField(default='none', upload_to='unknown'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='properties',
            name='pics3',
            field=models.FileField(default='x', upload_to='unknown'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='properties',
            name='pics',
            field=models.FileField(upload_to='unknown'),
        ),
    ]
