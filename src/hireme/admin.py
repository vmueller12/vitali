from django.contrib import admin

# Register your models here.
from .models import Hire

class HireAdmin(admin.ModelAdmin):
    list_display = ('project_name','name', 'contract', 'project', 'when', 'budget')
    
admin.site.register(Hire, HireAdmin)