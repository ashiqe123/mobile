from django import forms
from .models import test
class mobile_form(forms.ModelForm):
    class Meta:
        model= test
        fields=['type','brand','model','desc','img']