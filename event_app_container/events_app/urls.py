from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='event_list'),
    path('event-id', views.EventView.as_view()),
    path('organize-event', views.OrganizeEventView.as_view(), name='organize_event'),
    path('login-logout', views.LoginLogoutView.as_view(), name='login_logout'),
]