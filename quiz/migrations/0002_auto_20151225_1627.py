# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 10:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('correctly_answered_questions', models.IntegerField()),
                ('total_marks', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.AlterModelOptions(
            name='questionanswer',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='correct_answer',
            field=models.CharField(default=models.CharField(blank=True, max_length=75), max_length=75),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='option_w',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='option_x',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='option_y',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='option_z',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='topic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='questions_included',
            field=models.ManyToManyField(to='quiz.QuestionAnswer'),
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='subject',
            field=models.ManyToManyField(to='quiz.Subject'),
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
