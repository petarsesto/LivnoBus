from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vozni-red/', views.VozniRed, name='VozniRed'),
]