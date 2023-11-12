from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class ChangePass(forms.Form):
    pass_actual = forms.CharField(max_length=63, widget=forms.PasswordInput)
    nueva_pas1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    nueva_pas2 = forms.CharField(max_length=63, widget=forms.PasswordInput)

class SearchForm(forms.Form):
    search = forms.CharField()