# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('graffities', '0003_auto_20150717_2325'), ]

    operations = [
        migrations.AlterField(
            model_name='graffiti',
            name='comment',
            field=models.CharField(verbose_name='Комментарий',
                                   max_length=500), ),
        migrations.AlterField(
            model_name='graffiti',
            name='graffiti_type',
            field=models.CharField(choices=[('gr', 'Граффити'), (
                'sa', 'Уличное искусство'), ('pa', 'Паблик-Арт')],
                                   default='gr',
                                   verbose_name='Тип граффити',
                                   max_length=2), ),
    ]
