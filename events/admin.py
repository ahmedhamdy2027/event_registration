from django.contrib import admin
from .models import Event, Registration

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'organizer')  # Fields to display in the list view
    search_fields = ('title', 'description', 'location', 'organizer')  # Fields to search by
    list_filter = ('date', 'organizer')  # Filters to apply

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registration_date')  # Fields to display in the list view
    search_fields = ('user__username', 'event__title', 'email')  # Fields to search by
    list_filter = ('registration_date', 'event')  # Filters to apply

admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)
