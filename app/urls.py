from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_data, name='input_data'),
     path('', views.home, name='home'),
    path('display/', views.display_data, name='display_data'),
]
