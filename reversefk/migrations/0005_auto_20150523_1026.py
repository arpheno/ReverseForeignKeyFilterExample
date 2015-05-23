# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversefk', '0004_auto_20150523_1023'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orders',
            table='orders',
        ),
    ]
