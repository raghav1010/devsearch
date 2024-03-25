from django.urls import path
from . import views

urlpatterns = [
    path('notifications', views.push_notifications, name="push-notifications"),
]
