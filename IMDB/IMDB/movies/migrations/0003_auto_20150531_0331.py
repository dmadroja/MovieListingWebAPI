# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150531_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.CharField(default='Family', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
