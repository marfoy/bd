# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pub_date',
            field=models.TimeField(verbose_name='date published'),
        ),
    ]