# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afqmaps', '0034_auto_20150305_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afqmap',
            name='perc_bad_voxels',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
