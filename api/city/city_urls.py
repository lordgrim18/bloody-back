from django.urls import path
from .city_view import CityAPIView

urlpatterns = [
    path('all/', CityAPIView.as_view(), name='city_detail'), #get
    path('create/', CityAPIView.as_view(), name='city_create'), #single post
    
]