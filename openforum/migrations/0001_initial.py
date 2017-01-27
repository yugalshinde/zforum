# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-23 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.CharField(max_length=200)),
                ('answer_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=200)),
                ('comment_date', models.DateTimeField(verbose_name='Date published')),
                ('answer_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration_type', models.CharField(max_length=8)),
                ('down_vote', models.IntegerField(default=1)),
                ('up_vote', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_summary', models.CharField(max_length=64, verbose_name='Question Summary')),
                ('question_text', models.CharField(max_length=200, verbose_name='Question Text')),
                ('question_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_first_name', models.CharField(max_length=32, verbose_name='First name')),
                ('user_last_name', models.CharField(max_length=32, verbose_name='Last name')),
                ('user_email_address', models.CharField(max_length=128, verbose_name='Email address')),
                ('user_password', models.CharField(max_length=64, verbose_name='User password')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='question_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openforum.User'),
        ),
    ]