# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(default=b'upload_pics/default.jpg', upload_to=b'upload_pics/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='truesize',
            field=models.ImageField(default=b'upload_pics/default.jpg', upload_to=b'upload_pics/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='blacklists',
            field=models.ManyToManyField(related_name='blacklists_rel_+', to='photoapp.User', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='photoapp.User', blank=True),
            preserve_default=True,
        ),
    ]
