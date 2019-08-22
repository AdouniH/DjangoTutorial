
from django.forms import ModelForm
from .models import Visitor


class Log_form(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name']

