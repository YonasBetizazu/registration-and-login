from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

# Create a form to create a new user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] ='form-control form-control-lg'
        self.fields['email'].widget.attrs['class'] ='form-control form-control-lg'
        self.fields['password1'].widget.attrs['class'] ='form-control form-control-lg'
        self.fields['password2'].widget.attrs['class'] ='form-control form-control-lg'
    
#
class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=forms.TextInput (attrs={'class':'form-control form-control-lg'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}))

