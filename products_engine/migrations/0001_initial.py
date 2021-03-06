# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-05 18:25
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
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('ingredientes', models.TextField(blank=True, null=True, verbose_name='Ingredientes')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('valor', models.PositiveIntegerField(default=0, verbose_name='Valor')),
                ('calorias', models.CharField(blank=True, max_length=200, null=True, verbose_name='Calorias')),
                ('grasa', models.CharField(blank=True, max_length=200, null=True, verbose_name='Grasa')),
                ('zona', models.CharField(blank=True, max_length=200, null=True, verbose_name='Zona')),
                ('foto', models.ImageField(upload_to='uploads/platos/imagenes/', verbose_name='Foto')),
                ('shared', models.PositiveIntegerField(default=0, verbose_name='Compartidos')),
                ('comprados', models.PositiveIntegerField(default=0, verbose_name='Compras')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('fav', models.ManyToManyField(blank=True, null=True, related_name='Favorito', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps_plato', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Platos',
                'verbose_name': 'Plato',
            },
        ),
    ]
