# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151111_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to='C:\\Users\\Use\\Desktop\\vit\\src\\our_static\\media_root'),
        ),
    ]
