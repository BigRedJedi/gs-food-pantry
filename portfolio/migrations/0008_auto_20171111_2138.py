# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20171111_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='status',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
