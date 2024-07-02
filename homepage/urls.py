from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mapy-home'),
    path('about/', views.about, name='blog-about'),
]