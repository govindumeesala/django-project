from django.forms import ModelForm
from .models import *
class Interns_form(ModelForm):
    class Meta:
        model=Interns
        fields="__all__"
    