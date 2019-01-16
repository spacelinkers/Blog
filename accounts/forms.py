from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,UserChangeForm
)

from accounts.models import UserProfile

class RegisterFormView(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit = True):
        user = super(RegisterFormView, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            'password1',
            'password2',
            Submit('submit', 'Register')
        )

class EditProfileFormView(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class EditUserInfoFormView(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            'city',
            'website',
            'phone',
            'website',
            'description',
            'profile_image',
        )
