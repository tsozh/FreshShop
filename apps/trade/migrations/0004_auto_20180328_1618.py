# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-28 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20180328_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordergoods',
            options={'verbose_name': '订单商品', 'verbose_name_plural': '订单商品'},
        ),
    ]
