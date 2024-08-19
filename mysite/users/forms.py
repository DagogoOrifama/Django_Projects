from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# create a default user registration form, it inherit from the default
# user creation form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # the meta class hold info on the main class
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}
