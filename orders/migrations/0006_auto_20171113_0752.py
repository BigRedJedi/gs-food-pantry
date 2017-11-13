# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20171111_2148'),
        ('orders', '0005_auto_20171111_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='visit',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='portfolio.Visit'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]