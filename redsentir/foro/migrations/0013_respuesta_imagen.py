# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-17 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0012_auto_20180416_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to='static/images/foros'),
        ),
    ]
