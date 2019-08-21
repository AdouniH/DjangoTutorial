

from django.urls import path
from .views import main_page, disconnect, signup


urlpatterns = [
    path('', main_page, name='main_page'),
    path('signup/', signup, name='signup'),
    path('disconnect/', disconnect, name='disconnect')
]
