# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversefk', '0005_auto_20150523_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='country',
            field=models.CharField(default=b'country', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(default=b'size', max_length=255),
            preserve_default=True,
        ),
    ]
