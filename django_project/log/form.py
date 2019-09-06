
from django.forms import ModelForm, forms
from .models import Visitor, Token_rdv


class Log_form(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']

from django.forms import ModelForm

class TokenrdvForm(ModelForm):

    class Meta:
        model = Token_rdv
        fields = ('name', 'email', 'duration', 'commentaire')

    def __init__(self, *args, **kwargs):
        super(TokenrdvForm, self).__init__(*args, **kwargs)
        self.fields['commentaire'].required = False