

from django import forms

from .models import Conection


class DBForm(forms.ModelForm):
    class Meta:
        model = Conection
        fields = '__all__'
    
