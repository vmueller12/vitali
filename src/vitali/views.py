from django.views.generic import CreateView
from contact.forms import EmailForm


class HomeView(CreateView):
    template_name = 'vitali/index.html'
    form_class = EmailForm
    success_url = '/contact/thanks/'
    
