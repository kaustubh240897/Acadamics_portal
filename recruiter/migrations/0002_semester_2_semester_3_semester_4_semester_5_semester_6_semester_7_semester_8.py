# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-23 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=25)),
            ],
        ),
    ]
