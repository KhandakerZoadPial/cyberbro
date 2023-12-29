# admin.py

from django.contrib import admin
from .models import Organization, Volunteer

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'email', 'service_needed', 'user')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'number', 'user')
