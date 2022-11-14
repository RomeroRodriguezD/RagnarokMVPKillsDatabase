from django import forms
from django.forms import Select, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kills
import pandas as pd

class Registration(UserCreationForm):

    email = forms.EmailField(label='Your email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "email")  # No password field needed

    def save_user(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class MvpKill(forms.Form):

        model = Kills
        fields = ("name", "quantity")
        CHOICES = []
        listmvp = pd.read_csv('RagnarokDatabase/static/Lista MVP.csv')
        
        for row in listmvp.itertuples():
                CHOICES.append(row)
                
        name = forms.ChoiceField(choices=CHOICES)
        quantity = forms.IntegerField(required=False, initial=1)
        owner=""

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your email')

    class Meta:
        model = User
        fields = ("username", "email")
