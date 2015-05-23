# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reversefk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orders',
            table=None,
        ),
        migrations.AlterModelTable(
            name='size',
            table=None,
        ),
    ]
