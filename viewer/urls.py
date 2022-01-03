from django.urls import path, include
from viewer import views

urlpatterns = [
    path('', views.index),
    # Card details
    # Retrieve card using its database id
    path('details/<int:id>/', views.details),
    path('search/', views.search),
    path('contact/', views.contact)
]
