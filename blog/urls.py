from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # '': means we are at the home page
    path('about/', views.about, name='blog-about')
]
