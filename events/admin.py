
from django.contrib import admin
from .models import Event, Registration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'venue')
    search_fields = ('name', 'venue')
    list_filter = ('date',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'event')
    search_fields = ('name', 'email')
    list_filter = ('event',)
