# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]
