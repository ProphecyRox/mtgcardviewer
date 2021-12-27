from django.urls import path, include
from viewer import views

urlpatterns = [
    path('', views.index),
    path('details/<str:name>/', views.details)
]
