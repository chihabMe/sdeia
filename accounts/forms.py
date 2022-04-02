from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import Profile

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

class ProfileEditForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.widgets.TextInput(attrs={"class":'input--field boi--text'}))
    class Meta:
        model = Profile
        fields =['image','bio','website']

    def __init__(self,*args,**kwargs):
        super(ProfileEditForm,self).__init__(*args,**kwargs)
        self.fields['website'].widget.attrs.update({'class':'input--field'})