from django import forms 
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f'{value} is used.'), params= {'value' : value})
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='username or email')
    password = forms.CharField(widget=forms.PasswordInput)
    

    
    