# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-31 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_auto_20171027_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subTitulo', models.CharField(max_length=50, null=True)),
                ('parrafo1', models.TextField()),
                ('parrafo2', models.TextField()),
                ('parrafo3', models.TextField()),
                ('parrafo4', models.TextField()),
                ('parrafo5', models.TextField()),
                ('parrafo6', models.TextField()),
                ('imagen1', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('imagen2', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('imagen3', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('imagen4', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('video', models.CharField(max_length=50)),
                ('carreta1', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta2', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta3', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta4', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta5', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta6', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta7', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta8', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta9', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta10', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta11', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta12', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta13', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta14', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta15', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta16', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta17', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta18', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta19', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('carreta20', models.ImageField(upload_to='static/images/pagina/articulo')),
                ('entrevista1', models.CharField(max_length=50)),
                ('entrevista2', models.CharField(max_length=50)),
                ('entrevista3', models.CharField(max_length=50)),
                ('entrevista4', models.CharField(max_length=50)),
                ('entrevista5', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='noticia',
            old_name='descripcion',
            new_name='parrafo1',
        ),
        migrations.AddField(
            model_name='noticia',
            name='parrafo2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='parrafo3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
