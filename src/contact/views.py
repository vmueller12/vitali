from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin
# Create your views here.
from .forms import EmailForm

class EmailCreate(CreateView):
    template_name = 'contact/contact.html'
    success_url = '/contact/thanks/'
    form_class = EmailForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
              
        return super(EmailCreate, self).form_valid(form)
