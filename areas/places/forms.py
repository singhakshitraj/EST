from django import forms
from django.contrib.auth.models import User
from .models import Property

class NewUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class PropertyCreationForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name','description','price','image','square_foot','location','bhk','additional_bhk']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'price': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'square_foot': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'location': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
            'additional_bhk': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'}),
        }