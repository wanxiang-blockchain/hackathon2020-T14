from django.urls import path

from . import views

urlpatterns = [
    path('/get_all_bank', views.get_all_bank, name='index'),
    path('/get_client_info', views.get_client_info, name='index'),
    path('/get_all_billings', views.get_all_billings, name='index'),
    path('/client_certificate', views.client_certificate, name='index')
]