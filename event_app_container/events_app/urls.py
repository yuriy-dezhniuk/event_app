from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='view_events'),
    path('event-id', views.event),
    path('organize-event', views.organize_event, name='organize_event'),
    path('login-logout', views.login_logout, name='login_logout'),
]