# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151107_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
