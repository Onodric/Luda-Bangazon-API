# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bangazon_api', '0004_auto_20170127_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('date_of_birth', models.DateField(default=True)),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
    ]
