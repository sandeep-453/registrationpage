from django.urls import path
from .views import index
from .views import register

app_name = 'registration'

urlpatterns = [
    path('',index),
    path('api/register/', register, name='register'),
]
