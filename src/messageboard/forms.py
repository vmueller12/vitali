from django.forms import ModelForm
from .models import InputText


class TextFieldForm(ModelForm):
    class Meta:
        model = InputText
        fields = ['title', 'content']