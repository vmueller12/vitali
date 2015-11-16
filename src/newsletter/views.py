from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .forms import NewsletterForm

class NewsletterView(CreateView):
    template_name = 'contact/thanks.html'
    form_class = NewsletterForm
    success_url = '/contact/thanks/'

    
