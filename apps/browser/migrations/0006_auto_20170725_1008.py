# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-25 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0005_clicktask_pv'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='clicktask',
            table='click_task',
        ),
        migrations.AlterModelTable(
            name='taskcount',
            table='task_count',
        ),
        migrations.AlterModelTable(
            name='timetask',
            table='time_task',
        ),
    ]
