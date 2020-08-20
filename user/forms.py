from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from home.models import UserProfile
from django.utils.safestring import mark_safe
from django.forms import ModelForm,TextInput,Textarea,Select,FileInput

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields=('username','email','first_name','last_name')
        widgets = {
            'username': TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'email': TextInput(attrs={'class':'form-control','placeholder':'email'}),
            'first_name': TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name': TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
        }


CITY =[
    ('Istanbul','istanbul'),
    ('Ankara','ankara'),
    ('Izmir','izmir'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('phone','address','city','country','image')
        widgets = {
            'phone': TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'address': TextInput(attrs={'class':'form-control','placeholder':'address'}),
            'city': Select(attrs={'class':'form-control','placeholder':'city'},choices=CITY),
            'country': TextInput(attrs={'class':'form-control','placeholder':'country'}),
            'image': FileInput(attrs={'class':'form-control','placeholder':'image'}),
        }
