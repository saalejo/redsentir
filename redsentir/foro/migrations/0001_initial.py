# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-29 22:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduccion', models.CharField(max_length=20)),
                ('tema', models.CharField(max_length=200)),
                ('imagen', models.ImageField(default='static/images/foros/defaultUser.png', upload_to='static/images/foros/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foro.Foro'),
        ),
    ]
