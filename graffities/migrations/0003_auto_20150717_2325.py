# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms
import graffities.models


class Migration(migrations.Migration):

    dependencies = [('graffities', '0002_graffiti_legal'), ]

    operations = [
        migrations.AddField(
            model_name='graffiti',
            name='graffiti_type',
            field=models.CharField(max_length=2,
                                   default='gr',
                                   choices=[('gr', 'Граффити'), (
                                       'sa', 'Уличное искусство'), (
                                           'pa', 'Паблик-Арт')]), ),
        migrations.AlterField(
            model_name='graffiti',
            name='photo',
            field=django_resized.forms.ResizedImageField(
                upload_to=graffities.models.get_file_path,
                height_field='height',
                validators=[graffities.models.validate_image],
                width_field='width',
                verbose_name='Фото, jpg'), ),
    ]
