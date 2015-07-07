from django.forms import ModelForm
from captcha.fields import ReCaptchaField
from .models import Graffiti
from django.forms import widgets
from django.core.mail import EmailMultiAlternatives
from graffiti_map.settings import MANAGERS, DEFAULT_FROM_EMAIL

base_attr = {'class': 'form-control', 'required': ''}


class AddGraffitiForm(ModelForm):
    captcha = ReCaptchaField(label='Проверка')

    def send_email(self):
        msg = EmailMultiAlternatives(
            subject='Добавлено новое граффити!',
            body='Надо проверить!\nНазвание: %s\nОписание: %s\n' % (
                self.cleaned_data['name'], self.cleaned_data['comment']),
            from_email='Graffiti Map <%s>' % DEFAULT_FROM_EMAIL,
            to=MANAGERS, )
        msg.tags = ["new graffiti", ]
        msg.send()

    class Meta:
        model = Graffiti
        exclude = ('checked', 'active', 'legal')
        widgets = {
            'photo': widgets.FileInput(
                attrs={'accept': 'image/jpeg',
                       'required': ''}),
            'name': widgets.TextInput(attrs=base_attr),
            'comment': widgets.TextInput(attrs=base_attr),
            'lat': widgets.NumberInput(attrs=base_attr),
            'lon': widgets.NumberInput(attrs=base_attr),
        }
