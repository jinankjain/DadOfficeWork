# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeId', models.IntegerField(primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=200)),
                ('ratePerHour', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('noOfHours', models.FloatField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Employee')),
            ],
        ),
    ]
