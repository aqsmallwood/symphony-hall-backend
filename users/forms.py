from django.forms import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, blank=False)
    email = forms.CharField(max_length=100, blank=False)
    password = forms.CharField(max_length=50, blank=False)
    password_confirmation = forms.CharField(max_length=50, blank=False)