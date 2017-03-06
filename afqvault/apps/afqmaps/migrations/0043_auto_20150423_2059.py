# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import afqvault.apps.afqmaps.models


class Migration(migrations.Migration):

    dependencies = [
        ('afqmaps', '0042_auto_20150423_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='thumbnail',
            field=models.FileField(help_text=b'The orthogonal view thumbnail path of the nifti image', upload_to=afqvault.apps.afqmaps.models.upload_img_to, null=True, verbose_name=b'Image orthogonal view thumbnail (.png)', blank=True),
            preserve_default=True,
        ),
    ]