# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20151109_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
