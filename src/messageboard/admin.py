from django.contrib import admin

# Register your models here.
from .models import InputText, SentAnalysis, MachineLearning

class InputTextModel(admin.ModelAdmin):
    list_display = ("title", "content", "slug", "created",)
    prepopulated_fields = {"slug": ("title",)}
    
class SentModel(admin.ModelAdmin):
    list_display = ("__str__", "stopWords", "totalWords",)

admin.site.register(InputText, InputTextModel)
admin.site.register(SentAnalysis, SentModel)
admin.site.register(MachineLearning)

