# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 14:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100, verbose_name='配送区域')),
                ('address', models.CharField(max_length=100, verbose_name='详细地址')),
                ('signer_name', models.CharField(max_length=50, verbose_name='收货人')),
                ('signer_mobile', models.CharField(max_length=11, verbose_name='收货人电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户收货地址',
                'verbose_name': '用户收货地址',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户收藏',
                'verbose_name': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserLeaveMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购')], default=1, verbose_name='留言类型')),
                ('title', models.CharField(max_length=80, verbose_name='留言主题')),
                ('content', models.TextField(max_length=500, verbose_name='留言内容')),
                ('file', models.FileField(max_length=200, upload_to='user/leave/message/%Y/', verbose_name='上传文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户留言',
                'verbose_name': '用户留言',
            },
        ),
    ]