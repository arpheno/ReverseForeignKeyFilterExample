# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversefk', '0002_auto_20150523_1022'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orders',
            table='orders',
        ),
        migrations.AlterModelTable(
            name='size',
            table='size',
        ),
    ]
