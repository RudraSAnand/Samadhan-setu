from django.contrib import admin
from setu.models import Grievance, Contact  # Adjust if your app name is different

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'category', 'status', 'submitted_at']
    search_fields = ['name', 'email', 'category']
    list_filter = ['category', 'status', 'submitted_at']
    list_editable = ['status']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
