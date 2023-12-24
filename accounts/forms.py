from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', "last_name")


