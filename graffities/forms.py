from django.forms import ModelForm
from captcha.fields import ReCaptchaField
from .models import Graffiti

class AddGraffitiForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Graffiti
        exclude = ('checked', 'active')
