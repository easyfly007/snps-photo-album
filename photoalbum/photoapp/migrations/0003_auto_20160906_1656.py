# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0002_auto_20160601_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(blank=True, to='photoapp.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='photoapp.Tag'),
        ),
    ]
