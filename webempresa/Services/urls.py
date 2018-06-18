from django.urls import path
from . import views

urlpatterns = [
    # Path admin
    path('', views.services, name="services"),
]