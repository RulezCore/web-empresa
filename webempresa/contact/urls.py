from django.urls import path
from . import views

urlpatterns = [
    # Path admin
    path('', views.contact, name="contact"),
]