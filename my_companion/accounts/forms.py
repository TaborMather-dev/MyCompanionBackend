from django import forms
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    """This form allows our custom user model to be registered with an added field reflecting its Sitter status"""
    is_Sitter = forms.BooleanField(label="Check to register as Sitter", required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "is_Sitter")

    def save(self, commit=True):
        # Overriding the save method to add user to auth group of Sitter or Customer depending on if box is checked
        user = super(CustomUserForm, self).save(commit=False)
        user.is_Sitter = self.cleaned_data["is_Sitter"]

        # If you get an exception here, you need to create the Sitter/Customer groups in the Admin interface
        if commit:
            user.save()
            if user.is_Sitter:
                Sitters = Group.objects.get(name="Sitters")
                Sitters.user_set.add(user)
            else:
                customers = Group.objects.get(name="Customers")
                customers.user_set.add(user)
        return user


