from django.urls import path
from .views import home


app_name = 'turismo'

urlpatterns = [
    path('', home, name='home'),
]
