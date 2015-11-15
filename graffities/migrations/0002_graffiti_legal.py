# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('graffities', '0001_initial'), ]

    operations = [
        migrations.AddField(model_name='graffiti',
                            name='legal',
                            field=models.BooleanField(verbose_name='Легальное',
                                                      default=False), ),
    ]
