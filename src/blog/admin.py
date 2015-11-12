from django.contrib import admin

from .models import Entry, Tag
# Register your models here.
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)