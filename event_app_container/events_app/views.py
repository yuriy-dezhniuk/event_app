from django.shortcuts import render
from django.views.generic import ListView
# from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Event


class EventsListView(ListView):
    model = Event
    teplate_name = 'events_app/event_list.html'
    context_object_name = 'events'


class EventView(TemplateView):
    template_name = 'events_app/event.html'


class OrganizeEventView(TemplateView):
    template_name = 'events_app/organize_event.html'

# def login_logout(request):
#     return render(request, 'events_app/login_logout.html')
class LoginLogoutView(TemplateView):
    template_name = 'events_app/login_logout.html'

