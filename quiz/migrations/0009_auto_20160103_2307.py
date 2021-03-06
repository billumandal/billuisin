# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0008_auto_20151226_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'Fem', b'Female'), (b'Others', b'Others')], max_length=30, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('postal_code', models.PositiveIntegerField(null=True)),
                ('subject_name', models.CharField(choices=[(b'java', b'Java'), (b'dotnet', b'Asp.net'), (b'php', b'PHP'), (b'testing', b'Software Testing'), (b'python', b'Python'), (b'ruby', b'Ruby on Rails'), (b'cbasic', b'C Basic'), (b'oops', b'Object Oriented Programming')], max_length=17, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(choices=[(b'java', b'Java'), (b'dotnet', b'Asp.net'), (b'php', b'PHP'), (b'testing', b'Software Testing'), (b'python', b'Python'), (b'ruby', b'Ruby on Rails'), (b'cbasic', b'C Basic'), (b'oops', b'Object Oriented Programming')], max_length=17, null=True),
        ),
        migrations.RemoveField(
            model_name='quizattempt',
            name='subject',
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='subject',
            field=models.CharField(choices=[(b'java', b'Java'), (b'dotnet', b'Asp.net'), (b'php', b'PHP'), (b'testing', b'Software Testing'), (b'python', b'Python'), (b'ruby', b'Ruby on Rails'), (b'cbasic', b'C Basic'), (b'oops', b'Object Oriented Programming')], max_length=17, null=True),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
