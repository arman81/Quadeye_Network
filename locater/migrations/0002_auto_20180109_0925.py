# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacentre',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='datacentre',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10),
        ),
    ]
