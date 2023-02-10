from django.contrib import admin
from .models import Support

class SupportAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'name', 'subject', 'person', 'problem')
    list_display = ['name', 'subject', 'created_at']
    search_fields = ['subject']
    list_per_page = 10
admin.site.register(Support, SupportAdmin)