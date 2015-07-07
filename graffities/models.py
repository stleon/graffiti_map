import os
import uuid
from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField, delete
from django.core.files.base import ContentFile
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_file_path(instance, filename):
    filename = "%s.%s" % (uuid.uuid4(), filename.split('.')[-1].lower())
    return filename


def validate_image(image):
    "Валидатор, проверяем формат файла"
    if not str(image).lower().endswith(('.jpg', '.jpeg', )):
        raise ValidationError('Поддерживается только jpg!')


class Graffiti(models.Model):
    width = models.PositiveIntegerField(editable=False, )
    height = models.PositiveIntegerField(editable=False, )
    photo = ResizedImageField('Фото',
                              size=[2500, 1024],
                              upload_to=get_file_path,
                              height_field='height',
                              width_field='width',
                              validators=[validate_image])
    name = models.CharField('Название', max_length=50)
    comment = models.CharField('Комментарий', max_length=140)
    lat = models.FloatField('Географическая широта', )
    lon = models.FloatField('Географическая долгота', )
    active = models.BooleanField('Активное', default=True)
    checked = models.BooleanField('Проверенное', default=False)
    legal = models.BooleanField('Легальное', default=False)
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


@receiver(post_delete, sender=Graffiti)
def photo_post_delete_handler(sender, **kwargs):
    graffiti = kwargs['instance']
    storage, path = graffiti.photo.storage, graffiti.photo.path
    storage.delete(path)
    delete(path)
