# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-16 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0011_auto_20171213_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='mensaje',
            field=models.CharField(max_length=1000),
        ),
    ]
