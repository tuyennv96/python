from django.contrib import admin
from django.urls import path, re_path, include
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('cars', views.ListCreateCarView.as_view()),
    path('cars/<int:pk>', views.UpdateDeleteCarView.as_view()),
]
