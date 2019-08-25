

from django.urls import path
from .views import main_page, disconnect, mycv


urlpatterns = [
    path('', main_page, name='main_page'),
    path('disconnect/', disconnect, name='disconnect'),
    path('cv_houssem_adouni/', mycv, name='mycv')
]
