# chatbot/forms.py
from django import forms

class UserInputForm(forms.Form):
    user_message = forms.CharField(max_length=255)
