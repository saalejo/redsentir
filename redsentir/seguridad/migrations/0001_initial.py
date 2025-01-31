# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-18 17:13
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
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField(default=0)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, default=None, null=True)),
                ('telefono', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('avatar', models.ImageField(default='static/images/avatar/defaultUser.png', upload_to='static/images/avatar/')),
                ('genero', models.CharField(max_length=20, null=True)),
                ('es_experto', models.BooleanField(default=False)),
                ('es_joven', models.BooleanField(default=False)),
                ('es_actor', models.BooleanField(default=False)),
                ('agenda_cita', models.BooleanField(default=False)),
                ('municipio', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='seguridad.Municipio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
