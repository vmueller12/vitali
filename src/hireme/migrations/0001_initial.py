# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('budget', models.CharField(max_length=100)),
                ('contract', models.CharField(choices=[('gc', 'General Contractor'), ('sc', 'Subcontractor'), ('st', 'Short Term Contract'), ('lt', 'Long Term Contract'), ('ct', 'Consultant')], max_length=2)),
                ('project', models.CharField(choices=[('mw', 'Membership Website'), ('ec', 'Ecommerce'), ('ls', 'Landing & Sharing Page'), ('mc', 'Maintenance'), ('pw', 'Personal Website'), ('dw', 'Data Wrangling'), ('dp', 'Data Preprocessing'), ('dv', 'Data Visualization'), ('dp', 'Data Prediction'), ('rs', 'Recommender System'), ('sm', 'Something else...')], max_length=2)),
                ('duration', models.CharField(choices=[('1', '1 - 4 Weeks'), ('2', '1 - 8 Weeks'), ('3', '1 - 12 Weeks'), ('4', '6 Months'), ('5', '12 Months'), ('6', 'Undefined')], max_length=1)),
                ('when', models.CharField(choices=[('1', 'ASAP'), ('2', '2 Weeks'), ('3', '1 Month'), ('4', 'Flexible')], max_length=1)),
                ('technologies', models.CharField(choices=[('1', 'DJANGO'), ('2', 'WORDPRESS'), ('3', 'I do not know')], max_length=1)),
            ],
        ),
    ]
