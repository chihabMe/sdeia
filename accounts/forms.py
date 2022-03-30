from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.widgets.Input(attrs={"class":"input--field"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.Input(attrs={"class":"input--field"}))
    email  = forms.EmailField(widget=forms.widgets.EmailInput(attrs={"class":"input--field"}))
    password1 = forms.CharField(label='password',widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))
    password2 = forms.CharField(label='password confirmation',widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))

    def clean(self):
        if self.cleaned_data.get('password1')!=self.cleaned_data.get('password2'):
            raise ValidationError("please check your password confirmation again")
