from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event-id', views.event),
    path('organize-event', views.organize_event),
]