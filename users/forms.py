from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Contact


User = get_user_model()

'''
Форма регистрации
'''


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


'''
Форма для связи(добавлено условие "вежливости")
'''


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')

    def clean_subject(self):
        data = self.cleaned_data['subject']
        if "спасибо" not in data.lower():
            raise forms.ValidationError("Говорить спасибо - очень важно!")
        return data
