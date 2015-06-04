# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20150604_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.FloatField(),
        ),
    ]
