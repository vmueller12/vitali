# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
