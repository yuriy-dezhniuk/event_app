from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'description', 'event_data',)
    list_filter = ('event_data', 'id',)
    search_fields = ('title',)

admin.site.register(Event, EventAdmin)

