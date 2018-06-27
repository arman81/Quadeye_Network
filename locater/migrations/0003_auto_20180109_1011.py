# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locater', '0002_auto_20180109_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='dest_dc',
        ),
        migrations.RemoveField(
            model_name='link',
            name='src_dc',
        ),
        migrations.AlterField(
            model_name='link',
            name='latency',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10),
        ),
    ]
