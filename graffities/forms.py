from django.forms import ModelForm
from captcha.fields import ReCaptchaField
from .models import Graffiti
from django.forms import widgets

base_attr = {'class':'form-control', 'required':''}

class AddGraffitiForm(ModelForm):
    captcha = ReCaptchaField(label='Проверка')
    class Meta:
        model = Graffiti
        exclude = ('checked', 'active')
        widgets = {
            'photo': widgets.FileInput(attrs={'accept':
                'image/jpeg,image/png,image/gif', 'required':''}),
            'name': widgets.TextInput(attrs=base_attr),
            'comment': widgets.TextInput(attrs=base_attr),
            'lat': widgets.NumberInput(attrs=base_attr),
            'lon': widgets.NumberInput(attrs=base_attr),
        }
