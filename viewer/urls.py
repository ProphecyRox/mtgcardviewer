from django.urls import path, include
from viewer import views

urlpatterns = [
    path('', views.index),
]
