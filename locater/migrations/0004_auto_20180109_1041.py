# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locater', '0003_auto_20180109_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='ass_dc',
            field=models.ForeignKey(default=None, to='locater.dataCentre'),
        ),
        migrations.AddField(
            model_name='link',
            name='dc_type',
            field=models.CharField(default=b'NA', max_length=1, choices=[(b'source', b'source'), (b'dest', b'dest')]),
        ),
        migrations.AddField(
            model_name='link',
            name='linktype',
            field=models.CharField(default=b'NA', max_length=1, choices=[(b'Upcoming', b'Upcoming'), (b'Est', b'Est')]),
        ),
    ]
