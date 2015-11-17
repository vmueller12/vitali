from django.views.generic import CreateView


from .forms import HireForm


class HireView(CreateView):
    template_name = 'hireme/index.html'
    form_class = HireForm
    success_url = '/contact/thanks/'