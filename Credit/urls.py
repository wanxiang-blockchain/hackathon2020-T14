from django.urls import path

from . import views

urlpatterns = [
    path('/client', views.client, name='index'),
]