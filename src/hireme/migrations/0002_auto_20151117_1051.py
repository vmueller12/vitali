# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hire',
            name='project_name',
            field=models.CharField(max_length=128, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hire',
            name='technologies',
            field=models.CharField(choices=[('1', 'Django'), ('2', 'Wordpress'), ('3', "I don't know")], max_length=1),
        ),
    ]
