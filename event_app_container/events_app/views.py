from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import Event

# def index(request):
#     return render(request, 'events_app/view_events.html')

class EventsListView(ListView):
    model = Event
    teplate_name = 'events_app/event_list.html'
    context_object_name = 'events'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["event_list"] = Event.objects.all()
    #     return context

def event(request):
    return render(request, 'events_app/event.html')

def organize_event(request):
    return render(request, 'events_app/organize_event.html')

def login_logout(request):
    return render(request, 'events_app/login_logout.html')


