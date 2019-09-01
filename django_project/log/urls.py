

from django.urls import path
from .views import main_page, disconnect, mycv, rdv


urlpatterns = [
    path('', main_page, name='main_page'),
    path('disconnect/', disconnect, name='disconnect'),
    path('cv_houssem_adouni/<str:section>/', mycv, name='mycv'),
    path('rdv/<str:section>/', rdv, name='rdv')
]
