# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genere',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='pupularity',
            new_name='popularity',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='genere',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.ManyToManyField(related_name='genre', to='movies.Genre'),
        ),
    ]
