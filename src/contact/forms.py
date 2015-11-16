from django.forms import ModelForm
from .models import Email


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['name', 'subject', 'content']




