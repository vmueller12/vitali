from django.contrib import admin

# Register your models here.
from .models import InputText, SentAnalysis

class InputTextModel(admin.ModelAdmin):
    list_display = ("title", "content", "slug")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(InputText, InputTextModel)
admin.site.register(SentAnalysis)

