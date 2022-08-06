from django import forms
from .models import Features 


class Feature_Form(forms.ModelForm):
    class Meta :
        model = Features
        fields = '__all__'
    def __init__(self, *args, **kwargs):
            super(Feature_Form, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[str(field)].widget.attrs.update({'class': 'form-control'})
        