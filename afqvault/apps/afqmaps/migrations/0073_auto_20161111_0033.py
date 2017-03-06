# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import afqvault.apps.afqmaps.models
import afqvault.apps.afqmaps.storage


class Migration(migrations.Migration):

    dependencies = [
        ('afqmaps', '0072_auto_20161109_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='data_origin',
            field=models.CharField(default=b'volume', choices=[(b'volume', b'volume'), (b'surface', b'surface')], max_length=200, blank=True, help_text=b'Was this map originaly derived from volume or surface?', null=True, verbose_name=b'Data origin'),
        ),
        migrations.AlterField(
            model_name='image',
            name='surface_left_file',
            field=models.FileField(storage=afqvault.apps.afqmaps.storage.DoubleExtensionStorage(), upload_to=afqvault.apps.afqmaps.models.upload_img_to, null=True, verbose_name=b'File with the unthresholded LEFT hemisphere fsaverage surface map (.mgh)', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='surface_right_file',
            field=models.FileField(storage=afqvault.apps.afqmaps.storage.DoubleExtensionStorage(), upload_to=afqvault.apps.afqmaps.models.upload_img_to, null=True, verbose_name=b'File with the unthresholded RIGHT hemisphere fsaverage surface map (.mgh)', blank=True),
        ),
    ]