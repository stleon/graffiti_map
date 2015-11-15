import os
import uuid
from django.db import models
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError
from django_cleanup.signals import cleanup_pre_delete, cleanup_post_delete
from django.dispatch import receiver
from sorl.thumbnail import delete


def sorl_delete(**kwargs):
    from sorl.thumbnail import delete
    delete(kwargs['file'])


cleanup_pre_delete.connect(sorl_delete)


def get_file_path(instance, filename):
    filename = "%s.%s" % (uuid.uuid4(), filename.split('.')[-1].lower())
    return filename


def validate_image(image):
    "Валидатор, проверяем формат файла"
    if not str(image).lower().endswith(('.jpg', '.jpeg', )):
        raise ValidationError('Поддерживается только jpg!')


class Graffiti(models.Model):
    GRAFFITI_TYPE_CHOICES = (('gr', 'Граффити'),
                             ('sa', 'Уличное искусство'),
                             ('pa', 'Паблик-Арт'), )
    width = models.PositiveIntegerField(editable=False, )
    height = models.PositiveIntegerField(editable=False, )
    photo = ResizedImageField('Фото, jpg',
                              size=[2500, 1024],
                              upload_to=get_file_path,
                              height_field='height',
                              width_field='width',
                              validators=[validate_image])
    name = models.CharField('Название', max_length=50)
    comment = models.CharField('Комментарий', max_length=500)
    lat = models.FloatField('Географическая широта', )
    lon = models.FloatField('Географическая долгота', )
    active = models.BooleanField('Активное', default=True)
    checked = models.BooleanField('Проверенное', default=False)
    legal = models.BooleanField('Легальное', default=False)
    graffiti_type = models.CharField('Тип граффити',
                                     max_length=2,
                                     choices=GRAFFITI_TYPE_CHOICES,
                                     default='gr', )
    date_created = models.DateTimeField('Создано',
                                        auto_now_add=True,
                                        auto_now=False, )
    date_updated = models.DateTimeField('Обновлено',
                                        auto_now_add=False,
                                        auto_now=True, )

    def __str__(self):
        return '%s, %s' % (self.id, self.name)

    def get_absolute_url(self):
        return reverse('graffiti', kwargs={'pk': self.id, })

    class Meta:
        verbose_name = 'Граффити'
        verbose_name_plural = verbose_name
