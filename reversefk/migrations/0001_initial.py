# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('order_id', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=1)),
                ('brand_id', models.IntegerField()),
                ('user_id', models.IntegerField(default=6)),
                ('shop_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('item_gender', models.CharField(max_length=1)),
                ('return_reason', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('size', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'size',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orders',
            name='size',
            field=models.ForeignKey(to='reversefk.Size'),
            preserve_default=True,
        ),
    ]
