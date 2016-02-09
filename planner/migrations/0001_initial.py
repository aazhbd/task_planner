# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('status', models.CharField(default='To Do', max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
    ]
