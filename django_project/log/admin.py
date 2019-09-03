from django.contrib import admin
from .models import Visitor, RendezVous, Token_rdv
# Register your models here.

admin.site.register(Visitor)
admin.site.register(RendezVous)
admin.site.register(Token_rdv)