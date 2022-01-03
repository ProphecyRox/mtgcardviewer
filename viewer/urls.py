from django.urls import path, include
from viewer import views

urlpatterns = [
    path('', views.index),
    # Card details
    # Retrieve card using its database id
    path('details/<int:id>/', views.details, name="details"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact")
]
