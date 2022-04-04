from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.widgets.Input(attrs={"class":"input--field"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.widgets.Input(attrs={"class":"input--field"}))
    email  = forms.EmailField(widget=forms.widgets.EmailInput(attrs={"class":"input--field"}))
    password1 = forms.CharField(label='password',widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))
    password2 = forms.CharField(label='password confirmation',widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))
    class Meta:
        model = User 
        fields = ['username']
    def clean(self):
        if self.cleaned_data.get('password1')!=self.cleaned_data.get('password2'):
            raise ValidationError("please check your password confirmation again")

class ProfileEditForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.widgets.Textarea(attrs={"class":'boi--text input--field '}))
    class Meta:
        model = Profile
        fields =['image','bio','website']

    def __init__(self,*args,**kwargs):
        
        super(ProfileEditForm,self).__init__(*args,**kwargs)
        self.fields['website'].widget.attrs.update({'class':'input--field'})
        self.fields['image'].widget.attrs.update({"id":'image-change'})

class ProfilePasswordChangeForm(PasswordChangeForm):
    min_len=8

    def __init__(self,*args, **kwargs):
        super(ProfilePasswordChangeForm,self).__init__(*args,**kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'input--field'})
        self.fields['new_password1'].widget.attrs.update({'class':'input--field'})
        self.fields['new_password2'].widget.attrs.update({'class':'input--field'})

        self.fields['new_password1'].label='new password'
        self.fields['new_password2'].label='confirmation'
