from django import forms
from app.models import *

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}

class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']