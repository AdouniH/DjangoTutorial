
from django.forms import ModelForm
from .models import Visitor, Token_rdv


class Log_form(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']

from django.forms import ModelForm

class TokenrdvForm(ModelForm):
    class Meta:
        model = Token_rdv
        fields = '__all__'
