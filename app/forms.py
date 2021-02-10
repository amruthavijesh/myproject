
from django import forms
from .models import User

class UserRegForm(forms.ModelForm):

    Password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    Confirmpassword=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=8)
    class Meta():
        model = User
        fields = ('Firstname','Lastname','Gender','Address','Email','Photo','Place','Phone','Village','District','Password','Confirmpassword')

class UserLoginForm(forms.ModelForm):
    Password= forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('Email', 'Password')

class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('Firstname','Lastname','Gender','Address','Email','Photo','Place','Phone','Village','District')

class PasswordChangeForm(forms.Form):
    OldPassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)
    NewPassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=8)