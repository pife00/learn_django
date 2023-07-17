from django import forms;
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User;

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'  
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User;
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 
        'placeholder':'Your password',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 
        'placeholder':'Repeat password',
        'class':'w-full md:w-1/2 py-3 px-2 roundex-xl border border-gray-300'
    }))
    
    
    

