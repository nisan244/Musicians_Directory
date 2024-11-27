from django import forms
from . import models

    
class Album_Form(forms.ModelForm):
    class Meta:
        model = models.Album_Model
        fields = '__all__'
        
        
        
    levels = {
        'release_date' : 'Date'
    }