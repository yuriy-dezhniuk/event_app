from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'events_app/view_events.html')

def event(request):
    return render(request, 'events_app/event.html')

def organize_event(request):
    return render(request, 'events_app/organize_event.html')

def login_logout(request):
    return render(request, 'events_app/login_logout.html')


