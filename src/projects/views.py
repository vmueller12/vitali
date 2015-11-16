from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView



class ProjectView(TemplateView):
    
    template_name = 'project/index.html'