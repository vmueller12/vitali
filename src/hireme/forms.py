from django import forms

from .models import Hire


class HireForm(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ['project_name', 'contract', 'project', 'duration', 'when', 'technologies', 'budget', 'name', 'email', 'phone']

   
