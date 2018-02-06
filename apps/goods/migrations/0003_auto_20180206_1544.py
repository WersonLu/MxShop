# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_hotsearchwords_indexad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsimage',
            options={'verbose_name': '商品轮播图', 'verbose_name_plural': '商品轮播图'},
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterModelTable(
            name='goodscategorybrand',
            table=None,
        ),
    ]