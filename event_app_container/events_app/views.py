from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the page with full list of events")


def event(request):
    return HttpResponse("Hello, this is the page with separate event")

def create_event(request):
    return HttpResponse("Hello, this is the page for creating new events")
