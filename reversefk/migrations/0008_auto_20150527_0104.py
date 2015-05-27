# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversefk', '0007_auto_20150527_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_gender',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='return_reason',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shop_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(default=5),
            preserve_default=True,
        ),
    ]
