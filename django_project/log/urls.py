

from django.urls import path
from .views import main_page, disconnect, mycv, rdv, rdv_fix, form_submit, test


urlpatterns = [
    path('', main_page, name='main_page'),
    path('disconnect/', disconnect, name='disconnect'),
    path('cv_houssem_adouni/<str:section>/', mycv, name='mycv'),
    path('rdv/<str:section>/', rdv, name='rdv'),
    path('rdv/phone/take_rdv/<int:creneau_id>/', rdv_fix, name='rdv_fix'),
    path('rdv/phone/take_rdv/<int:creneau_id>/validation', form_submit, name='rdv_validation'),
    path('test/', test, name='test')
]
