# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afqmaps', '0032_migrate_cogatlas_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='afqmap',
            name='ignore_file_warning',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
