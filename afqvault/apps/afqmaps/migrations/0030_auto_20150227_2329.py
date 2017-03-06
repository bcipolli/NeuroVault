# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afqmaps', '0029_auto_20150227_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afqmap',
            name='contrast_definition_cogatlas',
            field=models.ForeignKey(to='afqmaps.CognitiveAtlasTask', max_length=200, blank=True, help_text=b"Link to <a href='http://www.cognitiveatlas.org/'>Cognitive Atlas</a> definition of this contrast", null=True, verbose_name=b'Cognitive Atlas definition'),
            preserve_default=True,
        ),
    ]
