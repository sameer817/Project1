from django import forms
from testapp.models import ContactModel, EmailModel, GenerateTextmodel
from django.contrib.auth.models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            "password" : forms.PasswordInput(),

        }

class GenerateTextmodelForm(forms.ModelForm):
    class Meta:
        model = GenerateTextmodel
        fields = '__all__'
