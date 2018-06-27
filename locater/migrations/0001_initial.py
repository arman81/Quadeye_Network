# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataCentre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=10)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkname', models.CharField(max_length=30)),
                ('dest_dc', models.CharField(max_length=10)),
                ('latency', models.DecimalField(max_digits=20, decimal_places=10)),
                ('src_dc', models.ForeignKey(to='locater.dataCentre')),
            ],
        ),
    ]
