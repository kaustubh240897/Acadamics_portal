# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-25 13:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0004_auto_20181024_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_pdfs', models.FileField(null=True, upload_to='')),
                ('video_link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('course_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Semester_1')),
            ],
        ),
    ]