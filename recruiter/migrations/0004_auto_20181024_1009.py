# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-24 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_auto_20181024_1007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Semester3',
            new_name='Semester_2',
        ),
        migrations.RenameModel(
            old_name='Semester2',
            new_name='Semester_3',
        ),
    ]
