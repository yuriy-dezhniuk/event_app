from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'events_app/list_of_events.html')

def event(request):
    return HttpResponse("Hello, this is the page with separate event")

def create_event(request):
    return HttpResponse("Hello, this is the page for creating new events")


