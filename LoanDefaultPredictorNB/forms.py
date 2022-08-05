from django import forms
from .models import Features 
from django.db import models


class Feature_Form(forms.ModelForm):
    class Meta :
        model = Features
        fields = '__all__'