# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import graffities.models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Graffiti',
            fields=[
                ('id', models.AutoField(primary_key=True,
                                        serialize=False,
                                        auto_created=True,
                                        verbose_name='ID')),
                ('width', models.PositiveIntegerField(editable=False)),
                ('height', models.PositiveIntegerField(editable=False)),
                ('photo',
                 models.ImageField(height_field='height',
                                   width_field='width',
                                   verbose_name='Фото',
                                   upload_to=graffities.models.get_file_path)),
                ('name', models.CharField(verbose_name='Название',
                                          max_length=50)),
                ('comment', models.CharField(verbose_name='Комментарий',
                                             max_length=140)),
                ('lat', models.FloatField(verbose_name='Географическая широта')
                 ),
                ('lon', models.FloatField(verbose_name=
                                          'Географическая долгота')),
                ('active', models.BooleanField(verbose_name='Активное',
                                               default=True)),
                ('checked', models.BooleanField(verbose_name='Проверенное',
                                                default=False)),
                ('date_created', models.DateTimeField(verbose_name='Создано',
                                                      auto_now_add=True)),
                ('date_updated', models.DateTimeField(verbose_name='Обновлено',
                                                      auto_now=True)),
            ],
            options={
                'verbose_name': 'Граффити',
                'verbose_name_plural': 'Граффити',
            }, ),
    ]
