from django import forms
from .models import Applay,job


class Applyform (forms.ModelForm):
    class Meta:
        model=Applay
        
        fields =['name','email','website','cv','cover']
        
        
class Addform (forms.ModelForm):
    class Meta:
        model = job 
        fields ='__all__'
        exclude =('slug','owner')
        
        