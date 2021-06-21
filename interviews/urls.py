from django.urls import path
from . import views

urlpatterns = [
    path('api/audio', views.getting_audio_from_user, name='interview'),
]
