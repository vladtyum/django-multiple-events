# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdate',
            old_name='question',
            new_name='event',
        ),
    ]
