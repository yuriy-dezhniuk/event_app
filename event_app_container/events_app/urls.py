from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('event-id', views.event),
    path('create-event', views.create_event),
]