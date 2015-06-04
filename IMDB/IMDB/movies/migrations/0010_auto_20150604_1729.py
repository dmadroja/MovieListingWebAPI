# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20150604_1722'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movies',
            unique_together=set([('name', 'director')]),
        ),
    ]
