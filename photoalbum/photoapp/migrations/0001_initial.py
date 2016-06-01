# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('title',),
            },
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('-time',),
            },
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10)),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('nickname', models.CharField(max_length=32)),
                ('pic', models.ImageField(default=b'profile_pics/default.jpg', upload_to=b'profile_pics/')),
                ('info', models.TextField()),
                ('administrator', models.BooleanField()),
                ('locked', models.BooleanField()),
                ('blacklists', models.ManyToManyField(related_name='blacklists_rel_+', to='photoapp.User')),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='photoapp.User')),
            ],
            options=None,
            bases=None,
            managers=None,
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='photoapp.Comment')),
            ],
            options=None,
            bases=('photoapp.comment',),
            managers=None,
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='photoapp.Comment')),
            ],
            options=None,
            bases=('photoapp.comment',),
            managers=None,
        ),
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(to='photoapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='photoapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='photoapp.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(related_name='photos', to='photoapp.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='tag',
            field=models.ManyToManyField(to='photoapp.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='photoapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='photoapp.Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photocomment',
            name='photo',
            field=models.ForeignKey(related_name='comments', to='photoapp.Photo'),
            preserve_default=True,
        ),
    ]
