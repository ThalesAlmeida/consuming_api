from django import forms
from django.forms import ModelForm
from .models import Turismo


class TurismoForm(ModelForm):
    class Meta:
        model = Turismo
        fields = '__all__'