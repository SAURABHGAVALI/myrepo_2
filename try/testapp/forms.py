from django import forms
from django.contrib.auth.models import User
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password','first_name','last_name']

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
