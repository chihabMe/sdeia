from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.widgets.Input(attrs={"class":"input--field"}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={"class":"input--field"}))

