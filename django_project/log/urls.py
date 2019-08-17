

from django.urls import path
from .views import main_page, disconnect


urlpatterns = [
    path('', main_page, name='main_page'),
    path('disconnect/', disconnect, name='disconnect')
]
